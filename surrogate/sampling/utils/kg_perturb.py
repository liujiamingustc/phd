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

import math

import numpy as np

def perturb(X, PertNum):
    """Interchanges pairs of randomly chosen elements within randomly
    chosen columns of a sampling plan a number of times. If the plan is
    a Latin hypercube, the result of this operation will also be a Latin
    hypercube.

    :param X: sampling plan
    :param PertNum: the number of changes (perturbations) to be made to X.
    :return: X perturbed sampling plan
    """
    X_pert = X.copy()
    [n, k] = np.shape(X_pert)

    for pert_count in range(0, PertNum):
        col = math.floor(np.random.rand(1) * k)

        # Choosing two distinct random points
        el1 = 0
        el2 = 0
        while el1 == el2:
            el1 = math.floor(np.random.rand(1) * n)
            el2 = math.floor(np.random.rand(1) * n)

        # swap the two chosen elements
        arrbuffer = X_pert[el1, col]
        X_pert[el1, col] = X_pert[el2, col]
        X_pert[el2, col] = arrbuffer

    return X_pert
