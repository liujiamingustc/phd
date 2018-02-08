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
