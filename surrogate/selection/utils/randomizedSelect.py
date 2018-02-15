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

from ._randomizedPartition import _randomizedPartition

def randomizedSelect(array, begin, end, i):
    """Allows to select the ith smallest element from array without sorting it.
    Runtime is expected to be O(n).
    """
    if begin == end:
        return array[begin]
    q = _randomizedPartition(array, begin, end)
    k = q - begin + 1
    if i < k:
        return randomizedSelect(array, begin, q, i)
    else:
        return randomizedSelect(array, q + 1, end, i - k)
