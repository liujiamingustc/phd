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
