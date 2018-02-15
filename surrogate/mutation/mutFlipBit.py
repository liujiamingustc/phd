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

def mutFlipBit(variable, prob=0.5):
    """Flip the value of the attributes of the input individual and return the
    mutant. The *individual* is expected to be a :term:`sequence` and the values of the
    attributes shall stay valid after the ``not`` operator is called on them.
    The *prob* argument is the probability of each attribute to be
    flipped. This mutation is usually applied on boolean individuals.

    :param variable: Decision Variable to be mutated.
    :param prob: Independent probability for each attribute to be flipped.
    :returns: A tuple of one variable.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i in xrange(len(variable)):
        # for i in xrange(variable.size):
        if random.random() < prob:
            variable[i] = type(variable[i])(not variable[i])

    return variable
