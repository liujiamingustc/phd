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

from surrogate.sampling import *

print '\nTest sampling.samFullFact: samFullFact'
print samFullFact([2, 4, 3])
print '\nTest sampling.samFullFact: samFF2n'
print samFF2n(3)
print '\nTest sampling.samFullFact: samFracFact'
print 'a b ab'
print samFracFact("a b ab")
print 'A B AB'
print samFracFact("A B AB")
print 'a b -ab c +abc'
print samFracFact("a b -ab c +abc")
