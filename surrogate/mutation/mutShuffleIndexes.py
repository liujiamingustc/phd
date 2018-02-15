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

def mutShuffleIndexes(variable, prob=0.5):
    """Shuffle the attributes of the input individual and return the mutant.
    The *individual* is expected to be a :term:`sequence`. The *prob* argument is the
    probability of each attribute to be moved. Usually this mutation is applied on
    vector of indices.

    :param variable: Decision Variable to be mutated.
    :param prob: Independent probability for each attribute to be exchanged to
                 another position.
    :returns: A tuple of one variable.

    This function uses the :func:`~random.random` and :func:`~random.randint`
    functions from the python base :mod:`random` module.
    """
    size = len(variable)
    # size = variable.size
    for i in xrange(size):
        if random.random() < prob:
            swap_indx = random.randint(0, size - 2)
            if swap_indx >= i:
                swap_indx += 1
            variable[i], variable[swap_indx] = \
                variable[swap_indx], variable[i]

    return variable
