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

from operator import itemgetter

from .sorNDHelperB import sorNDHelperB
from .utils import isDominated, sweepA, splitA

def sorNDHelperA(fitnesses, obj, front):
    """Create a non-dominated sorting of S on the first M objectives"""
    if len(fitnesses) < 2:
        return
    elif len(fitnesses) == 2:
        # Only two individuals, compare them and adjust front number
        s1, s2 = fitnesses[0], fitnesses[1]
        if isDominated(s2[:obj + 1], s1[:obj + 1]):
            front[s2] = max(front[s2], front[s1] + 1)
    elif obj == 1:
        sweepA(fitnesses, front)
    elif len(frozenset(map(itemgetter(obj), fitnesses))) == 1:
        # All individuals for objective M are equal: go to objective M-1
        sorNDHelperA(fitnesses, obj - 1, front)
    else:
        # More than two individuals, split list and then apply recursion
        best, worst = splitA(fitnesses, obj)
        sorNDHelperA(best, obj, front)
        sorNDHelperB(best, worst, obj - 1, front)
        sorNDHelperA(worst, obj, front)
