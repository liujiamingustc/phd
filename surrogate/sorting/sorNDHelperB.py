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

from .utils import isDominated, sweepB, splitB


def sorNDHelperB(best, worst, obj, front):
    """Assign front numbers to the solutions in H according to the solutions
    in L. The solutions in L are assumed to have correct front numbers and the
    solutions in H are not compared with each other, as this is supposed to
    happen after sorNDHelperB is called."""
    key = itemgetter(obj)
    if len(worst) == 0 or len(best) == 0:
        # One of the lists is empty: nothing to do
        return
    elif len(best) == 1 or len(worst) == 1:
        # One of the lists has one individual: compare directly
        for hi in worst:
            for li in best:
                if isDominated(hi[:obj + 1], li[:obj + 1]) or hi[:obj + 1] == li[:obj + 1]:
                    front[hi] = max(front[hi], front[li] + 1)
    elif obj == 1:
        sweepB(best, worst, front)
    elif key(min(best, key=key)) >= key(max(worst, key=key)):
        # All individuals from L dominate H for objective M:
        # Also supports the case where every individuals in L and H
        # has the same value for the current objective
        # Skip to objective M-1
        sorNDHelperB(best, worst, obj - 1, front)
    elif key(max(best, key=key)) >= key(min(worst, key=key)):
        best1, best2, worst1, worst2 = splitB(best, worst, obj)
        sorNDHelperB(best1, worst1, obj, front)
        sorNDHelperB(best1, worst2, obj - 1, front)
        sorNDHelperB(best2, worst2, obj, front)
