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

from .kg_jd import jd

def mmphi(X, q=2, p=1):
    """Calculates the sampling plan quality criterion of Morris and Mitchell

    :param X: Sampling plan
    :param q: exponent used in the calculation of the metric (default = 2)
    :param p: the distance metric to be used (p=1 rectangular - default , p=2 Euclidean)
    :return: Phiq - sampling plan 'space-fillingness' metric
    """
    # calculate the distances between all pairs of
    # points (using the p-norm) and build multiplicity array J
    J, d = jd(X, p)
    # the sampling plan quality criterion
    Phiq = (np.sum(J * (d ** (-q)))) ** (1.0 / q)
    return Phiq
