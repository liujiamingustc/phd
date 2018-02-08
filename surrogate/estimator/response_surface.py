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

"""Surrogate Model based on second order response surface equations."""

from numpy import zeros, einsum
from numpy.dual import lstsq

from surrogate.base import SurrogateModel


class RSurfaceSurrogate(SurrogateModel):
    """Response Surface Surrogate Model

    """
    def __init__(self):
        super(RSurfaceSurrogate, self).__init__()

        self.m = 0  # number of training points
        self.n = 0  # number of independents
        self.betas = zeros(0)  # vector of response surface equation coefficients

    def fit(self, x, y):
        """ Calculate response surface equation coefficients using least
        squares regression.

        :param x: Training input locations
        :type x: array-like

        :param y: Model responses at given inputs
        :type y: array-like
        """

        super(RSurfaceSurrogate, self).fit(x, y)

        m = self.m = x.shape[0]
        n = self.n = x.shape[1]

        X = zeros((m, ((n + 1) * (n + 2)) // 2))

        # Modify X to include constant, squared terms and cross terms

        # Constant Terms
        X[:, 0] = 1.0

        # Linear Terms
        X[:, 1:n + 1] = x

        # Quadratic Terms
        X_offset = X[:, n + 1:]
        for i in range(n):
            # Z = einsum('i,ij->ij', X, Y) is equivalent to, but much faster and
            # memory efficient than, diag(X).dot(Y) for vector X and 2D array Y.
            # I.e. Z[i,j] = X[i]*Y[i,j]
            X_offset[:, :n - i] = einsum('i,ij->ij', x[:, i], x[:, i:])
            X_offset = X_offset[:, n - i:]

        # Determine response surface equation coefficients (betas) using least squares
        self.betas, rs, r, s = lstsq(X, y)

    def predict(self, x):
        """Calculates a predicted value of the response based on the current
        response surface model for the supplied list of inputs.

        :param x: Point at which the surrogate is evaluated
        :type x: array-like
        """

        super(RSurfaceSurrogate, self).predict(x)

        n = x.size

        X = zeros(((self.n + 1) * (self.n + 2)) // 2)

        # Modify X to include constant, squared terms and cross terms

        # Constant Terms
        X[0] = 1.0

        # Linear Terms
        X[1:n + 1] = x

        # Quadratic Terms
        X_offset = X[n + 1:]
        for i in xrange(n):
            X_offset[:n - i] = x[i] * x[i:]
            X_offset = X_offset[n - i:]

        # Predict new_y using X and betas
        return X.dot(self.betas)

    def linearize(self, x):
        """Calculates the jacobian of the Kriging surface at the requested point.

        :param x: Point at which the surrogate Jacobian is evaluated
        :type x: array-like
        """
        n = self.n
        betas = self.betas

        x = x.flat

        jac = betas[1:n + 1, :].copy()
        beta_offset = betas[n + 1:, :]
        for i in xrange(n):
            jac[i, :] += x[i:].dot(beta_offset[:n - i, :])
            jac[i:, :] += x[i] * beta_offset[:n - i, :]
            beta_offset = beta_offset[n - i:, :]

        return jac.T
