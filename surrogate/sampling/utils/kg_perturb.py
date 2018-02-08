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
