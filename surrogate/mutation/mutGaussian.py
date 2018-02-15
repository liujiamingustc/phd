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
from collections import Sequence
from itertools import repeat

def mutGaussian(variable, mu=1, sigma=0.5, prob=0.5):
    """This function applies a gaussian mutation of mean *mu* and standard
    deviation *sigma* on the input individual. This mutation expects a
    :term:`sequence` individual composed of real valued attributes.
    The *prob* argument is the probability of each attribute to be mutated.

    :param variable: Decision Variable to be mutated.
    :param mu: Mean or :term:`python:sequence` of means for the
               gaussian addition mutation.
    :param sigma: Standard deviation or :term:`python:sequence` of
                  standard deviations for the gaussian addition mutation.
    :param prob: Independent probability for each attribute to be mutated.
    :returns: A tuple of one variable.

    This function uses the :func:`~random.random` and :func:`~random.gauss`
    functions from the python base :mod:`random` module.
    """
    size = len(variable)
    # size = variable.size
    if not isinstance(mu, Sequence):
        mu = repeat(mu, size)
    elif len(mu) < size:
        raise IndexError("mu must be at least the size of variable: %d < %d" % (len(mu), size))
    if not isinstance(sigma, Sequence):
        sigma = repeat(sigma, size)
    elif len(sigma) < size:
        raise IndexError("sigma must be at least the size of variable: %d < %d" % (len(sigma), size))

    for i, m, s in zip(xrange(size), mu, sigma):
        if random.random() < prob:
            variable[i] += random.gauss(m, s)

    return variable
