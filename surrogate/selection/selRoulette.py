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
from operator import attrgetter

def selRoulette(individuals, k=1):
    """Select *k* individuals from the input *individuals* using *k*
    spins of a roulette. The selection is made by looking only at the first
    objective of each individual. The list returned contains references to
    the input *individuals*.

    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    :returns: A list of selected individuals.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.

    .. warning::
       The roulette selection by definition cannot be used for minimization
       or when the fitness can be smaller or equal to 0.
    """
    s_inds = sorted(individuals, key=attrgetter("fitness"), reverse=True)
    # TODO 20161204 individual property fitness.values[]
    # sum_fits = sum(ind.fitness.values[0] for ind in individuals)
    sum_fits = sum(ind.fitness for ind in individuals)

    chosen = []
    for i in xrange(k):
        u = random.random() * sum_fits
        sum_ = 0
        for ind in s_inds:
            # sum_ += ind.fitness.values[0]
            sum_ += ind.fitness
            if sum_ > u:
                chosen.append(ind)
                break

    return chosen
