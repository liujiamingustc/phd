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
