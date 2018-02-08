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
