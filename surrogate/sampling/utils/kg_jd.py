# Copyright 2016 Quan Pan
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: Apache License, Version 2.0
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
