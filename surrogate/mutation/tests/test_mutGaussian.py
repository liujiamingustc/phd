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

from surrogate.mutation import mutGaussian

print '\nTest.mutation.mutGaussian: mutGaussian'
ind = np.array([x / 10.0 for x in range(0, 10, 1)])
print '\tInput:  ind=\t' + '\t'.join(map(str, ind)) + ''
out = mutGaussian(variable=ind.tolist())
print '\tOutput: out=\t' + '\t'.join(map(str, out)) + ''
