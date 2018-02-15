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

from .identity import identity

def median(seq, key=identity):
    """Returns the median of *seq* - the numeric value separating the higher
    half of a sample from the lower half. If there is an even number of
    elements in *seq*, it returns the mean of the two middle values.
    """
    sseq = sorted(seq, key=key)
    length = len(seq)
    if length % 2 == 1:
        return key(sseq[(length - 1) // 2])
    else:
        return (key(sseq[(length - 1) // 2]) + key(sseq[length // 2])) / 2.0
