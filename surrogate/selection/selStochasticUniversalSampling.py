# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
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
