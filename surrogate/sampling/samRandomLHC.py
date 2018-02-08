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


def samRandomLHC(n=2, k=2, Edges=0):
    """Generates a random latin hypercube within the [0,1]^k hypercube

    :param n: desired number of points
    :param k: number of design variables (dimensions)
    :param Edges: if Edges=1 the extreme bins will have their centers on the edges of the domain
    :returns: Latin hypercube sampling plan of n points in k dimensions
    """
    # pre-allocate memory
    X = np.zeros((n, k))

    # exclude 0

    for i in xrange(0, k):
        X[:, i] = np.transpose(np.random.permutation(np.arange(1, n + 1, 1)))

    if Edges == 1:
        X = (X - 1) / (n - 1)
    else:
        X = (X - 0.5) / n

    return X
