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

import unittest

import numpy as np

from surrogate.estimator import NNeighborSurrogate
from surrogate.util.test import assert_rel_error


class TestNearestNeighbor(unittest.TestCase):
    def test_unrecognized_type(self):
        with self.assertRaises(ValueError) as cm:
            NNeighborSurrogate(interpolant_type='junk')

        expected_msg = "NNeighborSurrogate: interpolant_type 'junk' not supported." \
                       " interpolant_type must be one of ['linear', 'weighted'," \
                       " 'rbf']."

        self.assertEqual(expected_msg, str(cm.exception))


class TestLinearInterpolator1D(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='linear')
        self.x = np.array([[0.], [1.], [2.], [3.]])
        self.y = np.array([[0.], [1.], [1.], [0.]])
        self.surrogate.fit(self.x, self.y)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.5], [1.], [0.5]])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_bulk_prediction(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.5], [1.], [0.5]])
        mu = self.surrogate.predict(test_x)
        assert_rel_error(self, mu, expected_y, 1e-9)

    def test_jacobian(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_deriv = np.array([[1.], [0.], [-1.]])

        for x0, y0 in zip(test_x, expected_deriv):
            jac = self.surrogate.linearize(x0)
            assert_rel_error(self, jac, y0, 1e-9)

    def test_pt_cache(self):
        test_x = np.array([[0.5]])

        self.surrogate.predict(test_x)

        # Mess with internals to ensure cache is being used.
        self.surrogate.interpolant._KData = None

        mu = self.surrogate.linearize(test_x)

        assert_rel_error(self, mu, np.array([[1.]]), 1e-6)


class TestLinearInterpolatorND(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='linear')
        self.x = np.array([[0., 0.], [2., 0.], [2., 2.], [0., 2.], [1., 1.]])
        self.y = np.array([[1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [0., 1., .5, 0.]])
        self.surrogate.fit(self.x, self.y)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])
        expected_y = np.array([[0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [1., 0., 0.5, 1.],
                               [0.5, 0.5, 0.5, 0.5]
                               ])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_bulk_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])
        expected_y = np.array([[0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [0.5, 0.5, 0.5, 0.5],
                               [1., 0., 0.5, 1.],
                               [0.5, 0.5, 0.5, 0.5]
                               ])

        mu = self.surrogate.predict(test_x)
        assert_rel_error(self, mu, expected_y, 1e-9)

    def test_jacobian(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.],
                           [1., 1.5],
                           [1.5, 1.]
                           ])
        expected_deriv = np.array([
            [[0., -1.], [0., 1.], [0., 0.], [0., -1.]],
            [[-1., 0.], [1., 0.], [0., 0.], [-1., 0.]],
            [[0., 1.], [0., -1.], [0., 0.], [0., 1.]],
            [[1., 0.], [-1., 0.], [0., 0.], [1., 0.]]
        ])

        for x0, y0 in zip(test_x, expected_deriv):
            mu = self.surrogate.linearize(x0)
            assert_rel_error(self, mu, y0, 1e-9)


class TestWeightedInterpolator1D(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='weighted')
        self.x = np.array([[0.], [1.], [2.], [3.]])
        self.y = np.array([[0.], [1.], [1.], [0.]])
        self.surrogate.fit(self.x, self.y)

    def test_insufficient_points(self):
        with self.assertRaises(ValueError) as cm:
            self.surrogate.predict(self.x[0], n=100)

        expected_msg = ('WeightedInterpolant does not have sufficient '
                        'training data to use n=100, only 4 points available.')

        self.assertEqual(str(cm.exception), expected_msg)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0, n=3)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.52631579], [0.94736842], [0.52631579]])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0, n=3)
            assert_rel_error(self, mu, y0, 1e-8)

    def test_bulk_prediction(self):

        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.52631579], [0.94736842], [0.52631579]])

        mu = self.surrogate.predict(test_x, n=3)
        assert_rel_error(self, mu, expected_y, 1e-8)

    def test_jacobian(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_deriv = np.array([[1.92797784], [0.06648199], [-1.92797784]])

        for x0, y0 in zip(test_x, expected_deriv):
            jac = self.surrogate.linearize(x0, n=3)
            assert_rel_error(self, jac, y0, 1e-6)

    def test_pt_cache(self):
        test_x = np.array([[0.5]])

        self.surrogate.predict(test_x, n=3)

        # Mess with internals to ensure cache is being used.
        self.surrogate.interpolant._KData = None

        mu = self.surrogate.linearize(test_x, n=3)

        assert_rel_error(self, mu, np.array([[1.92797784]]), 1e-6)


class TestWeightedInterpolatorND(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='weighted')
        self.x = np.array([[0., 0.], [2., 0.], [2., 2.], [0., 2.], [1., 1.]])
        self.y = np.array([[1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [0., 1., .5, 0.]])
        self.surrogate.fit(self.x, self.y)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])
        a = ((16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.))) /
             (16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.)) + 8.))

        b = 8. / (8. + 16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.)))
        c = (2. + 2. / (5. * np.sqrt(5))) / (3. + 2. / (5. * np.sqrt(5)))
        d = 1. / (3. + 2. / (5. * np.sqrt(5)))

        expected_y = np.array([[a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [c, d, 0.5, c],
                               [0.54872067, 0.45127933, 0.5, 0.54872067]
                               ])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0, n=5, dist_eff=3)
            assert_rel_error(self, mu, y0, 1e-6)

    def test_bulk_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])

        a = ((16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.))) /
             (16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.)) + 8.))
        b = 8. / (8. + 16. / (5 * np.sqrt(5.)) + 16. / (13. * np.sqrt(13.)))
        c = (2. + 2. / (5. * np.sqrt(5))) / (3. + 2. / (5. * np.sqrt(5)))
        d = 1. / (3. + 2. / (5. * np.sqrt(5)))

        expected_y = np.array([[a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [c, d, 0.5, c],
                               [0.54872067, 0.45127933, 0.5, 0.54872067]
                               ])

        mu = self.surrogate.predict(test_x, n=5, dist_eff=3)
        assert_rel_error(self, mu, expected_y, 1e-6)

    def test_jacobian(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.],
                           [1., 1.5],
                           [1.5, 1.]
                           ])
        a = 0.99511746
        expected_deriv = np.array([
            [[0., -a], [0., a], [0., 0.], [0., -a]],
            [[-a, 0], [a, 0.], [0., 0.], [-a, 0]],
            [[0., a], [0., -a], [0., 0.], [0., a]],
            [[a, 0.], [-a, 0.], [0., 0.], [a, 0.]]
        ])

        for x0, y0 in zip(test_x, expected_deriv):
            mu = self.surrogate.linearize(x0)
            assert_rel_error(self, mu, y0, 1e-6)


class TestRBFInterpolator1D(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='rbf', n=4)
        self.x = np.array([[0.], [1.], [2.], [3.]])
        self.y = np.array([[0.], [2.], [2.], [0.]])
        self.surrogate.fit(self.x, self.y)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.82893803], [1.72485853], [0.82893803]])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-8)

    def test_bulk_prediction(self):

        test_x = np.array([[0.5], [1.5], [2.5]])
        expected_y = np.array([[0.82893803], [1.72485853], [0.82893803]])

        mu = self.surrogate.predict(test_x)
        assert_rel_error(self, mu, expected_y, 1e-8)

    def test_jacobian(self):
        test_x = np.array([[0.5], [2.5]])
        expected_deriv = np.array([[2.34609214], [-2.34609214]])

        for x0, y0 in zip(test_x, expected_deriv):
            jac = self.surrogate.linearize(x0)
            assert_rel_error(self, jac, y0, 1e-6)

    def test_pt_cache(self):
        test_x = np.array([[0.5]])

        self.surrogate.predict(test_x)

        # Mess with internals to ensure cache is being used.
        self.surrogate.interpolant._KData = None

        mu = self.surrogate.linearize(test_x)

        assert_rel_error(self, mu, np.array([[2.34609214]]), 1e-6)


class TestRBFInterpolatorND(unittest.TestCase):
    def setUp(self):
        self.surrogate = NNeighborSurrogate(interpolant_type='rbf', n=5)
        self.x = np.array([[0., 0.], [2., 0.], [2., 2.], [0., 2.], [1., 1.]])
        self.y = np.array([[1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [1., 0., .5, 1.],
                           [0., 1., .5, 0.]])
        self.surrogate.fit(self.x, self.y)

    def test_training(self):
        for x0, y0 in zip(self.x, self.y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-9)

    def test_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])
        a = 0.05453616
        b = 0.5013363
        c = 0.33860606
        d = 0.13507662

        expected_y = np.array([[a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [c, d, 0.5, c],
                               [0.37840446, 0.336283, 0.5, 0.37840446]
                               ])

        for x0, y0 in zip(test_x, expected_y):
            mu = self.surrogate.predict(x0)
            assert_rel_error(self, mu, y0, 1e-6)

    def test_bulk_prediction(self):
        test_x = np.array([[1., 0.5],
                           [0.5, 1.0],
                           [1.0, 1.5],
                           [1.5, 1.],
                           [0., 1.],
                           [.5, .5]
                           ])

        a = 0.05453616
        b = 0.5013363
        c = 0.33860606
        d = 0.13507662

        expected_y = np.array([[a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [a, b, 0.5, a],
                               [c, d, 0.5, c],
                               [0.37840446, 0.336283, 0.5, 0.37840446]
                               ])

        mu = self.surrogate.predict(test_x)
        assert_rel_error(self, mu, expected_y, 1e-6)

    def test_jacobian(self):
        test_x = np.array([[0.5, 0.5],
                           [0.5, 1.5],
                           [1.5, 1.5],
                           [1.5, 0.5]
                           ])
        a = -0.97153433
        b = -0.97153433
        c = 0.59055939
        d = 0.59055939

        expected_deriv = np.array([
            [[a, b], [c, d], [0., 0.], [a, b]],
            [[a, -b], [c, -d], [0., 0.], [a, -b]],
            [[-a, -b], [-c, -d], [0., 0.], [-a, -b]],
            [[-a, b], [-c, d], [0., 0.], [-a, b]]
        ])

        for x0, y0 in zip(test_x, expected_deriv):
            mu = self.surrogate.linearize(x0)
            assert_rel_error(self, mu, y0, 1e-6)


if __name__ == "__main__":
    unittest.main()
