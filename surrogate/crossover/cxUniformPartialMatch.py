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


def cxUniformPartialMatch(var1, var2, prob=0.5):
    """Executes a uniform partially matched crossover (UPMX) on the input
    individuals. The two individuals are modified in place. This crossover
    expects :term:`sequence` individuals of indices, the result for any other
    type of individuals is unpredictable.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :param prob: Independent probabily for each attribute to be exchanged.
    :returns: A tuple of two variables.

    Moreover, this crossover generates two children by matching
    pairs of values chosen at random with a probability of *indpb* in the two
    parents and swapping the values of those indexes. For more details see
    [Cicirello2000]_.

    This function uses the :func:`~random.random` and :func:`~random.randint`
    functions from the python base :mod:`random` module.

    .. [Cicirello2000] Cicirello and Smith, "Modeling GA performance for
       control parameter optimization", 2000.
    """
    size = min(len(var1), len(var2))
    # size = min(var1.size, var2.size)
    p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for i in xrange(size):
        p1[var1[i]] = i
        p2[var2[i]] = i

    for i in xrange(size):
        if random.random() < prob:
            # Keep track of the selected values
            temp1 = var1[i]
            temp2 = var2[i]
            # Swap the matched value
            var1[i], var1[p1[temp2]] = temp2, temp1
            var2[i], var2[p2[temp1]] = temp1, temp2
            # Position bookkeeping
            p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
            p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return var1, var2
