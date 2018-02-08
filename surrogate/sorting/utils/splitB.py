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

from .median import median


def splitB(best, worst, obj):
    """Split both best individual and worst sets of fitnesses according
    to the median of objective *obj* computed on the set containing the
    most elements. The values equal to the median are attributed so as
    to balance the four resulting sets as much as possible.
    """
    median_ = median(best if len(best) > len(worst) else worst, itemgetter(obj))
    best1_a, best2_a, best1_b, best2_b = [], [], [], []
    for fit in best:
        if fit[obj] > median_:
            best1_a.append(fit)
            best1_b.append(fit)
        elif fit[obj] < median_:
            best2_a.append(fit)
            best2_b.append(fit)
        else:
            best1_a.append(fit)
            best2_b.append(fit)

    worst1_a, worst2_a, worst1_b, worst2_b = [], [], [], []
    for fit in worst:
        if fit[obj] > median_:
            worst1_a.append(fit)
            worst1_b.append(fit)
        elif fit[obj] < median_:
            worst2_a.append(fit)
            worst2_b.append(fit)
        else:
            worst1_a.append(fit)
            worst2_b.append(fit)

    balance_a = abs(len(best1_a) - len(best2_a) + len(worst1_a) - len(worst2_a))
    balance_b = abs(len(best1_b) - len(best2_b) + len(worst1_b) - len(worst2_b))

    if balance_a <= balance_b:
        return best1_a, best2_a, worst1_a, worst2_a
    else:
        return best1_b, best2_b, worst1_b, worst2_b
