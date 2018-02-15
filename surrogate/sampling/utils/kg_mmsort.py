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
