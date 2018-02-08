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


def cxBlend(var1, var2, alpha=0.5):
    """Executes a blend crossover that modify in-place the input individuals.
    The blend crossover expects :term:`sequence` individuals of floating point
    numbers.

    :param var1: The first variable participating in the crossover.
    :param var2: The second variable participating in the crossover.
    :param alpha: Extent of the interval in which the new values can be drawn
                  for each attribute on both side of the parents' attributes.
    :returns: A tuple of two variables.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """
    for i, (x1, x2) in enumerate(zip(var1, var2)):
        gamma = (1. + 2. * alpha) * random.random() - alpha
        var1[i] = (1. - gamma) * x1 + gamma * x2
        var2[i] = gamma * x1 + (1. - gamma) * x2

    return var1, var2
