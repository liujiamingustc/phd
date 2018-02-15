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
