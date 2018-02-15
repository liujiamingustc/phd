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

"""
This code was originally published by the following individuals for use with
Scilab:
    Copyright (C) 2012 - 2013 - Michael Baudin
    Copyright (C) 2012 - Maria Christopoulou
    Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
    Copyright (C) 2009 - Yann Collette
    Copyright (C) 2009 - CEA - Jean-Marc Martinez

    website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

Much thanks goes to these individuals. It has been converted to Python by
Abraham Lee.
"""

import numpy as np

def union(H1, H2):
    """Join two matrices by stacking them on top of each other.

    :param H1: The matrix that goes on top of the new matrix
    :param H2: The matrix that goes on bottom of the new matrix

    :returns: The new matrix that contains the rows of ``H1`` on top of the rows of
              ``H2``.

    :Example:

    >>> union(np.eye(2), -np.eye(2))
    array([[ 1.,  0.],
           [ 0.,  1.],
           [-1.,  0.],
           [ 0., -1.]])

    """
    H = np.r_[H1, H2]
    return H
