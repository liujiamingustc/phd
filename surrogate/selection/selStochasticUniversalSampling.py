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

def selStochasticUniversalSampling(individuals, k=1):
    """Select the *k* individuals among the input *individuals*.
    The selection is made by using a single random value to sample all of the
    individuals by choosing them at evenly spaced intervals. The list returned
    contains references to the input *individuals*.

    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    :return: A list of selected individuals.

    This function uses the :func:`~random.uniform` function from the python base
    :mod:`random` module.
    """
    s_inds = sorted(individuals, key=attrgetter("fitness"), reverse=True)
    # TODO 20161205 individual property fitness.values[]
    # sum_fits = sum(ind.fitness.values[0] for ind in individuals)
    sum_fits = sum(ind.fitness for ind in individuals)

    distance = sum_fits / float(k)
    start = random.uniform(0, distance)
    points = [start + i * distance for i in xrange(k)]

    chosen = []
    for p in points:
        i = 0
        # TODO 20161205 individual property fitness.values[]
        # sum_ = s_inds[i].fitness.values[0]
        sum_ = s_inds[i].fitness
        while sum_ < p:
            i += 1
            # TODO 20161205 individual property fitness.values[]
            # sum_ += s_inds[i].fitness.values[0]
            sum_ += s_inds[i].fitness
        chosen.append(s_inds[i])

    return chosen
