# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

import itertools
import unittest

from numpy import array, linspace, sin, cos, pi

from surrogate.estimator import KrigingSurrogate
from surrogate.util.test import assert_rel_error


def branin(x):
    y = (x[1] - (5.1 / (4. * pi ** 2.)) * x[0] ** 2. + 5. * x[0] / pi - 6.) ** 2. + 10. * (1. - 1. / (8. * pi)) * cos(
        x[0]) + 10.
    return y


def branin_1d(x):
    return branin(array([x[0], 2.275]))


class TestKrigingSurrogate(unittest.TestCase):
    def test_1d_training(self):
        x = array([[0.0], [2.0], [3.0], [4.0], [6.0]])
        y = array([[branin_1d(case)] for case in x])

        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

    def test_1d_predictor(self):
        x = array([[0.0], [2.0], [3.0], [4.0], [6.0]])
        y = array([[branin_1d(case)] for case in x])

        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)

        new_x = array([pi])
        mu, sigma = surrogate.predict(new_x)

        assert_rel_error(self, mu, 0.397887, 1e-1)
        assert_rel_error(self, sigma, 0.0294172, 1e-2)

    def test_1d_ill_conditioned(self):
        # Test for least squares solver utilization when ill-conditioned
        x = array([[case] for case in linspace(0., 1., 40)])
        y = sin(x)
        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)
        new_x = array([0.5])
        mu, sigma = surrogate.predict(new_x)

        self.assertTrue(sigma < 1.1e-8)
        assert_rel_error(self, mu, sin(0.5), 1e-6)

    def test_2d(self):
        x = array([[-2., 0.], [-0.5, 1.5], [1., 3.], [8.5, 4.5], [-3.5, 6.], [4., 7.5], [-5., 9.], [5.5, 10.5],
                   [10., 12.], [7., 13.5], [2.5, 15.]])
        y = array([[branin(case)] for case in x])

        surrogate = KrigingSurrogate()
        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

        mu, sigma = surrogate.predict([5., 5.])

        assert_rel_error(self, mu, branin([5., 5.]), 1e-1)
        assert_rel_error(self, sigma, 5.79, 1e-2)

    def test_no_training_data(self):
        surrogate = KrigingSurrogate()

        try:
            surrogate.predict([0., 1.])
        except RuntimeError as err:
            self.assertEqual(str(err),
                             "KrigingSurrogate has not been trained, "
                             "so no prediction can be made.")
        else:
            self.fail("RuntimeError Expected")

    def test_one_pt(self):
        surrogate = KrigingSurrogate()
        x = [[0.]]
        y = [[1.]]

        with self.assertRaises(ValueError) as cm:
            surrogate.fit(x, y)

        self.assertEqual(str(cm.exception), 'KrigingSurrogate require at least'
                                            ' 2 training points.')

    def test_vector_input(self):
        surrogate = KrigingSurrogate()

        x = array([[0., 0., 0.], [1., 1., 1.]])
        y = array([[0.], [3.]])

        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

    def test_vector_output(self):
        surrogate = KrigingSurrogate()

        y = array([[0., 0.], [1., 1.], [2., 0.]])
        x = array([[0.], [2.], [4.]])

        surrogate.fit(x, y)

        for x0, y0 in zip(x, y):
            mu, sigma = surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)
            assert_rel_error(self, sigma, 0, 1e-6)

    def test_scalar_derivs(self):
        surrogate = KrigingSurrogate()

        x = array([[0.], [1.], [2.], [3.]])
        y = x.copy()

        surrogate.fit(x, y)
        jac = surrogate.linearize(array([[0.]]))

        assert_rel_error(self, jac[0][0], 1., 1e-3)

    def test_vector_derivs(self):
        surrogate = KrigingSurrogate()

        x = array([[a, b] for a, b in
                   itertools.product(linspace(0, 1, 10), repeat=2)])
        y = array([[a + b, a - b] for a, b in x])

        surrogate.fit(x, y)
        jac = surrogate.linearize(array([[0.5, 0.5]]))
        assert_rel_error(self, jac, array([[1, 1], [1, -1]]), 1e-5)

if __name__ == "__main__":
    unittest.main()
