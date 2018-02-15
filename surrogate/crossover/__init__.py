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

from .cxOnePoint import cxOnePoint
from .cxTwoPoint import cxTwoPoint
from .cxUniform import cxUniform
from .cxPartialMatch import cxPartialyMatch
from .cxUniformPartialMatch import cxUniformPartialMatch
from .cxOrdered import cxOrdered
from .cxBlend import cxBlend
from .cxSimulatedBinary import cxSimulatedBinary
from .cxSimulatedBinaryBounded import cxSimulatedBinaryBounded
from .cxMessyOnePoint import cxMessyOnePoint

__all__ = [
    'cxOnePoint', 'cxTwoPoint', 'cxUniform',
    'cxPartialyMatch', 'cxUniformPartialMatch',
    'cxOrdered', 'cxBlend',
    'cxSimulatedBinary', 'cxSimulatedBinaryBounded',
    'cxMessyOnePoint'
]
