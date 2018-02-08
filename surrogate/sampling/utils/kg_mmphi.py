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


import numpy as np

from .kg_jd import jd

def mmphi(X, q=2, p=1):
    """Calculates the sampling plan quality criterion of Morris and Mitchell

    :param X: Sampling plan
    :param q: exponent used in the calculation of the metric (default = 2)
    :param p: the distance metric to be used (p=1 rectangular - default , p=2 Euclidean)
    :return: Phiq - sampling plan 'space-fillingness' metric
    """
    # calculate the distances between all pairs of
    # points (using the p-norm) and build multiplicity array J
    J, d = jd(X, p)
    # the sampling plan quality criterion
    Phiq = (np.sum(J * (d ** (-q)))) ** (1.0 / q)
    return Phiq
