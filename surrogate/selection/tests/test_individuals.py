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

from surrogate.base import Individual

def Individuals(n=10):
    return [
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=10.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=9.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=8.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=7.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=6.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=5.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=4.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=3.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=2.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=1.0, constrain=[])
    ]
