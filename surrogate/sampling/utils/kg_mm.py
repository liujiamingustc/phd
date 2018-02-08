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
