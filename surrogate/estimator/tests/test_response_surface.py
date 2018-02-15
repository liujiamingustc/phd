# Copyright 2016 Quan Pan
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: Apache License, Version 2.0
# Create: 2016-12-02

# pylint: disable-msg=C0111,C0103

import itertools
import unittest

from numpy import array, linspace, sin, cos, pi

from surrogate.estimator import RSurfaceSurrogate
from surrogate.util.test import assert_rel_error


def branin(x):
    y = (x[1] - (5.1 / (4. * pi ** 2.)) * x[0] ** 2. + 5. * x[0] / pi - 6.) ** 2. + 10. * (1. - 1. / (8. * pi)) * cos(
        x[0]) + 10.
    return y


def branin_1d(x):
    return branin(array([x[0], 2.275]))


class TestResponseSurfaceSurrogate(unittest.TestCase):
    def test_1d_training(self):

        x = array([[0.0], [2.0], [3.0]])
        y = array([[branin_1d(case)] for case in x])
        surrogate = RSurfaceSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_1d_predictor(self):
        x = array([[0.0], [2.0], [3.0], [4.0], [6.0]])
        y = array([[branin_1d(case)] for case in x])

        surrogate = RSurfaceSurrogate()
        surrogate.fit(x, y)

        new_x = array([pi])
        mu = surrogate.predict(new_x)

        assert_rel_error(self, mu, 1.73114, 1e-4)

    def test_1d_ill_conditioned(self):
        # Test for least squares solver utilization when ill-conditioned
        x = array([[case] for case in linspace(0., 1., 40)])
        y = sin(x)
        surrogate = RSurfaceSurrogate()
        surrogate.fit(x, y)
        new_x = array([0.5])
        mu = surrogate.predict(new_x)

        assert_rel_error(self, mu, sin(0.5), 1e-3)

    def test_2d(self):

        x = array([[-2., 0.], [-0.5, 1.5], [1., 1.], [0., .25], [.25, 0.], [.66, .33]])
        y = array([[branin(case)] for case in x])

        surrogate = RSurfaceSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

        mu = surrogate.predict(array([.5, .5]))

        assert_rel_error(self, mu, branin([.5, .5]), 1e-1)

    def test_no_training_data(self):
        surrogate = RSurfaceSurrogate()

        try:
            surrogate.predict([0., 1.])
        except RuntimeError as err:
            self.assertEqual(str(err),
                             "RSurfaceSurrogate has not been trained, so no prediction can be made.")
        else:
            self.fail("RuntimeError Expected")

    def test_one_pt(self):
        surrogate = RSurfaceSurrogate()
        x = array([[0.]])
        y = array([[1.]])

        surrogate.fit(x, y)
        assert_rel_error(self, surrogate.betas, array([[1.], [0.], [0.]]), 1e-9)

    def test_vector_input(self):
        surrogate = RSurfaceSurrogate()

        x = array([[0., 0., 0.], [1., 1., 1.]])
        y = array([[0.], [3.]])

        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_vector_output(self):
        surrogate = RSurfaceSurrogate()

        x = array([[0.], [2.], [4.]])
        y = array([[0., 0.], [1., 1.], [2., 0.]])

        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_scalar_derivs(self):
        surrogate = RSurfaceSurrogate()

        x = array([[0.], [1.], [2.], [3.]])
        y = x.copy()

        surrogate.fit(x, y)
        jac = surrogate.linearize(array([[0.]]))

        assert_rel_error(self, jac[0][0], 1., 1e-3)

    def test_vector_derivs(self):
        surrogate = RSurfaceSurrogate()

        x = array([[a, b] for a, b in
                   itertools.product(linspace(0, 1, 10), repeat=2)])
        y = array([[a + b, a - b] for a, b in x])

        surrogate.fit(x, y)
        jac = surrogate.linearize(array([[0.5, 0.5]]))
        assert_rel_error(self, jac, array([[1, 1], [1, -1]]), 1e-5)


if __name__ == "__main__":
    unittest.main()
