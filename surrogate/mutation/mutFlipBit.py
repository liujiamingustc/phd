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
