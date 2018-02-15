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

import numpy as np

def cxOnePoint(var1, var2):
    """Executes a one point crossover on the input :term:`sequence` individuals.
    The two individuals are modified in place. The resulting individuals will
    respectively have the length of the other.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.randint` function from the
    python base :mod:`random` module.
    """
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    cxpoint = np.random.randint(1, size - 1)
    var1[cxpoint:], var2[cxpoint:] = var2[cxpoint:], var1[cxpoint:]
    # var1[cxpoint:], var2[cxpoint:] = var2[cxpoint:].copy(), var1[cxpoint:].copy()

    return var1, var2
