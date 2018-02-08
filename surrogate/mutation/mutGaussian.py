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
