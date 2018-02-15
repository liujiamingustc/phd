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

from .kg_mmphi import mmphi
from .kg_perturb import perturb

def mmlhs(X_start, population, iterations, q):
    """Evolutionary operation search for the most space filling Latin hypercube
    of a certain size and dimensionality. There is no need to call this
    directly - use bestlh.m
    """
    X_s = X_start.copy()

    n = np.size(X_s, 0)

    X_best = X_s

    Phi_best = mmphi(X_best)

    leveloff = math.floor(0.85 * iterations)

    for it in range(0, iterations):
        if it < leveloff:
            mutations = int(round(1 + (0.5 * n - 1) * (leveloff - it) / (leveloff - 1)))
        else:
            mutations = 1

        X_improved = X_best
        Phi_improved = Phi_best

        for offspring in range(0, population):
            X_try = perturb(X_best, mutations)
            Phi_try = mmphi(X_try, q)

            if Phi_try < Phi_improved:
                X_improved = X_try
                Phi_improved = Phi_try

        if Phi_improved < Phi_best:
            X_best = X_improved
            Phi_best = Phi_improved

    return X_best
