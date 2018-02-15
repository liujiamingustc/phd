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
