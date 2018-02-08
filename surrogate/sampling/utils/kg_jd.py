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

from .kg_ismember import ismember

def jd(X, p=1):
    """Computes the distances between all pairs of points in a sampling plan
    X using the p-norm, sorts them in ascending order and removes multiple occurences.

    :param X: sampling plan being evaluated
    :param p: distance norm (p=1 rectangular-default, p=2 Euclidean)
    :returns: J-multiplicity array (that is, the number of pairs separated by each distance value)
              distinct_d-list of distinct distance values
    """
    # number of points in the sampling plan
    n = np.size(X[:, 1])

    # computes the distances between all pairs of points
    d = np.zeros((n * (n - 1) / 2))

    #    for i in xrange(n-1):
    #        for j in xrange(i+1,n):
    #            if i == 0:
    #                d[i+j-1] = np.linalg.norm((rld[0,:]-rld[j,:]),2)
    #            else:
    #                d[((i-1)*n - (i-1)*i/2 + j - i  )] = np.linalg.norm((X[i,:] - X[j,:]),2)

    # an alternative way of the above loop
    list = [(i, j) for i in xrange(n - 1) for j in xrange(i + 1, n)]
    for k, l in enumerate(list):
        d[k] = np.linalg.norm((X[l[0], :] - X[l[1], :]), p)

    # remove multiple occurences
    distinct_d = np.unique(d)

    # pre-allocate memory for J
    J = np.zeros(np.size(distinct_d))

    # generate multiplicity array
    for i in xrange(len(distinct_d)):
        # J(i) will contain the number of pairs separated
        # by the distance distinct_d(i)
        J[i] = np.sum(ismember(d, distinct_d[i]))

    return J, distinct_d
