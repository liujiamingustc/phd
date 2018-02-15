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

def cxMessyOnePoint(var1, var2):
    """Executes a one point crossover on :term:`sequence` individual.
    The crossover will in most cases change the individuals size. The two
    individuals are modified in place.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.randint` function from the python base
    :mod:`random` module.
    """
    cxpoint1 = random.randint(0, len(var1))
    cxpoint2 = random.randint(0, len(var2))
    # cxpoint1 = random.randint(0, var1.size)
    # cxpoint2 = random.randint(0, var2.size)
    var1[cxpoint1:], var2[cxpoint2:] = var2[cxpoint2:], var1[cxpoint1:]
    # var1[cxpoint1:], var2[cxpoint1:] = var2[cxpoint1:].copy(), var1[cxpoint1:].copy()

    return var1, var2
