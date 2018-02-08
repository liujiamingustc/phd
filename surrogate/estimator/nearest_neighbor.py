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

# Based off of the N-Dimensional Interpolation library by Stephen Marone.
# https://github.com/SMarone/NDInterp

from collections import OrderedDict

from surrogate.base import SurrogateModel
from surrogate.util.NDInterp import LinearInterpolator, WeightedInterpolator, RBFInterpolator

_interpolators = OrderedDict([
    ('linear', LinearInterpolator),
    ('weighted', WeightedInterpolator),
    ('rbf', RBFInterpolator),
])


class NNeighborSurrogate(SurrogateModel):
    """Surrogate model that approximates values using a nearest neighbor
    approximation. `interpolant_type` argument must be one of 'linear',
    'weighted', or 'rbf'.

    :param interpolant_type: One of 'linear', 'weighted', or 'rbf'. Determines the type of
                             interpolant used.
    :param kwargs: Additional keyword arguments to be passed to the constructor for the
                   interpolant.
    """

    def __init__(self, interpolant_type='rbf', **kwargs):
        super(NNeighborSurrogate, self).__init__()

        if interpolant_type not in _interpolators.keys():
            msg = "NNeighborSurrogate: interpolant_type '{0}' not supported." \
                  " interpolant_type must be one of {1}.".format(
                interpolant_type, list(_interpolators.keys())
            )
            raise ValueError(msg)

        self.interpolant_init_args = kwargs

        self.interpolant_type = interpolant_type
        self.interpolant = None

    def fit(self, x, y):
        """Train the surrogate model with the given set of inputs and outputs.

        :param x: Training input locations
        :param y: Model responses at given inputs.
        """
        super(NNeighborSurrogate, self).fit(x, y)
        self.interpolant = _interpolators[self.interpolant_type](x, y, **self.interpolant_init_args)

    def predict(self, x, **kwargs):
        """Calculates a predicted value of the response based on the current
        trained model for the supplied list of inputs.

        :param x: Point(s) at which the surrogate is evaluated.
        :param kwargs: Additional keyword arguments passed to the interpolant.
        """
        super(NNeighborSurrogate, self).predict(x)
        return self.interpolant(x, **kwargs)

    def linearize(self, x, **kwargs):
        """Calculates the jacobian of the interpolant at the requested point.

        :param x: Point at which the surrogate Jacobian is evaluated.
        :param kwargs: Additional keyword arguments passed to the interpolant.
        """
        jac = self.interpolant.gradient(x, **kwargs)
        if jac.shape[0] == 1 and len(jac.shape) > 2:
            return jac[0, ...]
        return jac
