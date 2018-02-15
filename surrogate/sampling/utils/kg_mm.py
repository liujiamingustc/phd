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

def mm(X1, X2, p=1):
    """Given two sampling plans chooses the one with the better space-filling properties
    (as per the Morris-Mitchell criterion)

    :param X1: the two sampling plans
    :param X2: the two sampling plans
    :param p: the distance metric to be used (p=1 rectangular-default, p=2 Euclidean)
    :return: Mmplan-if Mmplan=0, identical plans or equally space-
             filling, if Mmplan=1, X1 is more space filling, if Mmplan=2,
             X2 is more space filling
    """
    # thats how two arrays are compared in their sorted form
    v = np.sort(X1) == np.sort(X2)
    if v.all() == True:  # if True, then the designs are the same
        #    if np.array_equal(X1,X2) == True:
        return 0
    else:
        # calculate the distance and multiplicity arrays
        [J1, d1] = jd(X1, p);
        m1 = len(d1)
        [J2, d2] = jd(X2, p);
        m2 = len(d2)

        # blend the distance and multiplicity arrays together for
        # comparison according to definition 1.2B. Note the different
        # signs - we are maximising the d's and minimising the J's.
        V1 = np.zeros((2 * m1))
        V1[0:len(V1):2] = d1
        V1[1:len(V1):2] = -J1

        V2 = np.zeros((2 * m2))
        V2[0:len(V2):2] = d2
        V2[1:len(V2):2] = -J2

        # the longer vector can be trimmed down to the length of the shorter one
        m = min(m1, m2)
        V1 = V1[0:m]
        V2 = V2[0:m]

        # generate vector c such that c(i)=1 if V1(i)>V2(i), c(i)=2 if V1(i)<V2(i)
        # c(i)=0 otherwise
        c = np.zeros(m)
        for i in xrange(m):
            if np.greater(V1[i], V2[i]) == True:
                c[i] = 1
            elif np.less(V1[i], V2[i]) == True:
                c[i] = 2
            elif np.equal(V1[i], V2[i]) == True:
                c[i] = 0

        # If the plans are not identical but have the same space-filling
        # properties
        if sum(c) == 0:
            return 0
        else:
            # the more space-filling design (mmplan)
            # is the first non-zero element of c
            i = 0
            while c[i] == 0:
                i = i + 1
            return c[i]
