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
