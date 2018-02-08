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

from .kg_mm import mm

def mmsort(X3D, p=1):
    """Ranks sampling plans according to the Morris-Mitchell criterion definition.
    Note: similar to phisort, which uses the numerical quality criterion Phiq
    as a basis for the ranking.

    :param X3D: three-dimensional array containing the sampling plans to be ranked.
    :param p: the distance metric to be used (p=1 rectangular - default, p=2 Euclidean)
    :return: Index - index array containing the ranking
    """
    # Pre-allocate memory
    Index = np.arange(np.size(X3D, axis=2))

    # Bubble-sort
    swap_flag = 1

    while swap_flag == 1:
        swap_flag = 0
        i = 1
        while i <= len(Index) - 2:
            if mm(X3D[:, :, Index[i]], X3D[:, :, Index[i + 1]], p) == 2:
                arrbuffer = Index[i]
                Index[i] = Index[i + 1]
                Index[i + 1] = arrbuffer
                swap_flag = 1
            i = i + 1
        return Index
