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
