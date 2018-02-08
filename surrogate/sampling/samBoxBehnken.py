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

from .samFullFact import samFF2n
from .utils.doe_repeatCenter import repeatCenter


def samBoxBehnken(n, center=None):
    """Create a Box-Behnken design

    :param n: The number of factors in the design
    :param center: The number of center points to include (default = 1).
    :return: The design matrix

    This code was originally published by the following individuals for use with
    Scilab:

    - Copyright (C) 2012 - 2013 - Michael Baudin
    - Copyright (C) 2012 - Maria Christopoulou
    - Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
    - Copyright (C) 2009 - Yann Collette
    - Copyright (C) 2009 - CEA - Jean-Marc Martinez

    website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

    Much thanks goes to these individuals. It has been converted to Python by
    Abraham Lee.

    :Example:

    >>> samBoxBehnken(3)
    array([[-1., -1.,  0.],
           [ 1., -1.,  0.],
           [-1.,  1.,  0.],
           [ 1.,  1.,  0.],
           [-1.,  0., -1.],
           [ 1.,  0., -1.],
           [-1.,  0.,  1.],
           [ 1.,  0.,  1.],
           [ 0., -1., -1.],
           [ 0.,  1., -1.],
           [ 0., -1.,  1.],
           [ 0.,  1.,  1.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])

    """
    assert n >= 3, 'Number of variables must be at least 3'

    # First, compute a factorial DOE with 2 parameters
    H_fact = samFF2n(2)
    # Now we populate the real DOE with this DOE

    # We made a factorial design on each pair of dimensions
    # - So, we created a factorial design with two factors
    # - Make two loops
    Index = 0
    nb_lines = (n * (n - 1) / 2) * H_fact.shape[0]
    H = repeatCenter(n, nb_lines)

    for i in range(n - 1):
        for j in range(i + 1, n):
            Index = Index + 1
            H[max([0, (Index - 1) * H_fact.shape[0]]):Index * H_fact.shape[0], i] = H_fact[:, 0]
            H[max([0, (Index - 1) * H_fact.shape[0]]):Index * H_fact.shape[0], j] = H_fact[:, 1]

    if center is None:
        if n <= 16:
            points = [0, 0, 0, 3, 3, 6, 6, 6, 8, 9, 10, 12, 12, 13, 14, 15, 16]
            center = points[n]
        else:
            center = n

    H = np.c_[H.T, repeatCenter(n, center).T].T

    return H
