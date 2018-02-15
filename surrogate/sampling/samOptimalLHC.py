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

import os
import pickle

import numpy as np

from .samRandomLHC import samRandomLHC
from .utils import mmlhs, mmsort

# from surrogate.sampling.samRandomLHC import samRandomLHC
# from surrogate.sampling.utils import mmlhs, mmsort

def samOptimalLHC(n=2, k=2, population=30, iterations=30, generation=False):
    """Generates an optimized Latin hypercube by optimizing the Morris-Mitchell
    criterion for a range of exponents and plots the first two dimensions of
    the current hypercube throughout the optimization process.

    :param n: number of points required
    :param Population: number of individuals in the evolutionary operation
                       optimizer
    :param Iterations: number of generations the evolutionary operation
                       optimizer is run for
    :returns: X optimized Latin hypercube

    .. note::
        high values for the two inputs above will ensure high quality
        hypercubes, but the search will take longer.
        generation - if set to True, the LHC will be generated. If 'False,' the algorithm will check for an existing plan before generating.

    """
    PATH = os.path.dirname(os.path.abspath(__file__)) + '/sampling_plans/'
    # print PATH

    if not generation:
        # Check for existing LHC sampling plans
        if os.path.isfile('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n)):
            X = pickle.load(open('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n), 'r'))
            return X
        else:
            print PATH + '\nSampling Plans not found on disk, generating it now.'

    # list of qs to optimise Phi_q for
    q = [1, 2, 5, 10, 20, 50, 100]

    # Set the distance norm to rectangular for a faster search. This can be
    # changed to p=2 if the Euclidean norm is required.
    p = 1

    # we start with a random Latin hypercube
    XStart = samRandomLHC(n=n, k=k)

    X3D = np.zeros((n, k, len(q)))
    # for each q optimize Phi_q
    for i in xrange(len(q)):
        print ('Now_optimizing_for_q = %d' % q[i])

        X3D[:, :, i] = mmlhs(XStart, population, iterations, q[i])

    # sort according to the Morris-Mitchell criterion
    Index = mmsort(X3D, p)
    print ('Best_lh_found_using_q = %d' % q[Index[1]])

    # and the Latin hypercube with the best space-filling properties is

    X = X3D[:, :, Index[1]]
    pickle.dump(X, open('{0}lhc_{1}_{2}.pkl'.format(PATH, k, n), 'wb'))

    return X
