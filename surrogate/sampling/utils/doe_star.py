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

def star(n, alpha='faced', center=(1, 1)):
    """Create the star points of various design matrices

    :param n: The number of variables in the design
    :param alpha: Available values are 'faced' (default), 'orthogonal', or 'rotatable'
    :param center: A 1-by-2 array of integers indicating the number of center points
                   assigned in each block of the response surface design. Default is
                   (1, 1).
    :returns: H The star-point portion of the design matrix (i.e. at +/- alpha)
              a The alpha value to scale the star points with.

    :Example:

    >>> star(3)
    array([[-1.,  0.,  0.],
           [ 1.,  0.,  0.],
           [ 0., -1.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0., -1.],
           [ 0.,  0.,  1.]])

    """
    # Star points at the center of each face of the factorial
    if alpha == 'faced':
        a = 1
    elif alpha == 'orthogonal':
        nc = 2 ** n  # factorial points
        nco = center[0]  # center points to factorial
        na = 2 * n  # axial points
        nao = center[1]  # center points to axial design
        # value of alpha in orthogonal design
        a = (n * (1 + nao / float(na)) / (1 + nco / float(nc))) ** 0.5
    elif alpha == 'rotatable':
        nc = 2 ** n  # number of factorial points
        a = nc ** (0.25)  # value of alpha in rotatable design
    else:
        raise ValueError('Invalid value for "alpha": {:}'.format(alpha))

    # Create the actual matrix now.
    H = np.zeros((2 * n, n))
    for i in range(n):
        H[2 * i:2 * i + 2, i] = [-1, 1]

    H *= a

    return H, a
