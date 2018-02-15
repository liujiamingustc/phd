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

import random

def cxSimulatedBinary(var1, var2, eta=15):
    """Executes a simulated binary crossover that modify in-place the input
    individuals. The simulated binary crossover expects :term:`sequence`
    individuals of floating point numbers.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :param eta: Crowding degree of the crossover. A high eta will produce
                children resembling to their parents, while a small eta will
                produce solutions much more different.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i, (x1, x2) in enumerate(zip(var1, var2)):
        rand = random.random()
        if rand <= 0.5:
            beta = 2. * rand
        else:
            beta = 1. / (2. * (1. - rand))
        beta **= 1. / (eta + 1.)
        var1[i] = 0.5 * (((1 + beta) * x1) + ((1 - beta) * x2))
        var2[i] = 0.5 * (((1 - beta) * x1) + ((1 + beta) * x2))

    return var1, var2
