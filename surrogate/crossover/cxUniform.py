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

def cxUniform(var1, var2, prob=0.5):
    """Executes a uniform crossover that modify in place the two
    :term:`sequence` individuals. The attributes are swapped accordingto the
    *indpb* probability.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :param prob: Independent probabily for each attribute to be exchanged.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    for i in xrange(size):
        if random.random() < prob:
            var1[i], var2[i] = var2[i], var1[i]

    return var1, var2
