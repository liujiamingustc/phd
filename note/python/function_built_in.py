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

"""
https://docs.python.org/2/library/functions.html
"""

# super(type[, object-or-type])

import operator
import random


def uniform(low, high, size=None):
    try:
        return [random.uniform(a, b) for a, b in zip(low, high)]
    except TypeError:
        return [random.uniform(a, b) for a, b in zip([low] * size, [high] * size)]


_Ndim = 10
values = uniform(low=0.0, high=1.0, size=_Ndim)
# weights = [-1.0, -1.0]
weights = uniform(low=0.0, high=1.0, size=_Ndim)
result1 = tuple(map(operator.mul, values, weights))
print result1

a = [1, 2, 3, 4]
b = [10, 11, 12, 13]
result2 = list(map(operator.mul, a, b))
print result2
