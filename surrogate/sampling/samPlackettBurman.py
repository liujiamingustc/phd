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
from scipy.linalg import toeplitz, hankel


def samPlackettBurman(n):
    """Generate a Plackett-Burman design

    :param n: The number of factors to create a matrix for.
    :returns: An orthogonal design matrix with n columns, one for each factor, and
              the number of rows being the next multiple of 4 higher than n (e.g.,
              for 1-3 factors there are 4 rows, for 4-7 factors there are 8 rows,
              etc.)

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

    A 3-factor design:

    >>> samPlackettBurman(3)
    array([[-1., -1.,  1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1.,  1.]])

    A 5-factor design:

    >>> samPlackettBurman(5)
    array([[-1., -1.,  1., -1.,  1.],
           [ 1., -1., -1., -1., -1.],
           [-1.,  1., -1., -1.,  1.],
           [ 1.,  1.,  1., -1., -1.],
           [-1., -1.,  1.,  1., -1.],
           [ 1., -1., -1.,  1.,  1.],
           [-1.,  1., -1.,  1., -1.],
           [ 1.,  1.,  1.,  1.,  1.]])
    """
    assert n > 0, 'Number of factors must be a positive integer'
    keep = int(n)
    n = 4 * (int(n / 4) + 1)  # calculate the correct number of rows (multiple of 4)
    f, e = np.frexp([n, n / 12., n / 20.])
    k = [idx for idx, val in enumerate(np.logical_and(f == 0.5, e > 0)) if val]

    assert isinstance(n, int) and k != [], 'Invalid inputs. n must be a multiple of 4.'

    k = k[0]
    e = e[k] - 1

    if k == 0:  # N = 1*2**e
        H = np.ones((1, 1))
    elif k == 1:  # N = 12*2**e
        H = np.vstack((np.ones((1, 12)), np.hstack((np.ones((11, 1)),
                                                    toeplitz([-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1],
                                                             [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1])))))
    elif k == 2:  # N = 20*2**e
        H = np.vstack((np.ones((1, 20)), np.hstack((np.ones((19, 1)),
                                                    hankel(
                                                        [-1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1,
                                                         1],
                                                        [1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1,
                                                         -1])
                                                    ))))

    # Kronecker product construction
    for i in range(e):
        H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))

    # Reduce the size of the matrix as needed
    H = H[:, 1:(keep + 1)]

    return np.flipud(H)
