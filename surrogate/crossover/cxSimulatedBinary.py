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


def cxSimulatedBinary(var1, var2, eta=15):
    """Executes a simulated binary crossover that modify in-place the input
    individuals. The simulated binary crossover expects :term:`sequence`
    individuals of floating point numbers.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :param eta: Crowding degree of the crossover. A high eta will produce
                children resembling to their parents, while a small eta will
                produce solutions much more different.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i, (x1, x2) in enumerate(zip(var1, var2)):
        rand = random.random()
        if rand <= 0.5:
            beta = 2. * rand
        else:
            beta = 1. / (2. * (1. - rand))
        beta **= 1. / (eta + 1.)
        var1[i] = 0.5 * (((1 + beta) * x1) + ((1 - beta) * x2))
        var2[i] = 0.5 * (((1 - beta) * x1) + ((1 + beta) * x2))

    return var1, var2
