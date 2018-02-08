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

from surrogate.crossover import cxTwoPoint

print '\nTest.crossover.cxTwoPoint: cxTwoPoint'
ind1 = np.array(range(0, 10))
ind2 = np.array(range(10, 20))
# ind2 = np.array(range(9,-1,-1))
print '\tInput:  ind1_desVar=\t' + '\t'.join(map(str, ind1)) + ''
print '\tInput:  ind2_desVar=\t' + '\t'.join(map(str, ind2)) + ''
[out1, out2] = cxTwoPoint(var1=ind1.tolist(), var2=ind2.tolist())
print '\tOutput: out1_desVar=\t' + '\t'.join(map(str, out1)) + ''
print '\tOutput: out2_desVar=\t' + '\t'.join(map(str, out2)) + ''
