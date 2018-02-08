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

from math import ceil

import numpy as np
from scipy.spatial import cKDTree


class NNBase(object):
    """Base class for common functionality between nearest neighbor interpolants.
    """

    def __init__(self, training_points, training_values, num_leaves=2):
        """
        Initialize the nearest neighbor interpolant by scaling input to the
        unit hypercube.

        Args
        ----
        training_points : ndarray
            ndarray of shape (num_points x independent dims) containing
            training inpit locations.

        training_values : ndarray
            ndarray of shape (num_points x dependent dims) containing
            training output values.

        """
        # training_points and training_values are the known points and their
        # respective values which will be interpolated against.
        # Grab the mins and ranges of each dimension
        self._tpm = np.amin(training_points, axis=0)
        self._tpr = (np.amax(training_points, axis=0) - self._tpm)
        self._tvm = np.amin(training_values, axis=0)
        self._tvr = (np.amax(training_values, axis=0) - self._tvm)

        # This prevents against collinear data (range = 0)
        self._tpr[self._tpr == 0] = 1
        self._tvr[self._tvr == 0] = 1

        # Normalize all points
        self._tp = (training_points - self._tpm) / self._tpr
        self._tv = (training_values - self._tvm) / self._tvr

        # Record number of dimensions and points
        self._indep_dims = training_points.shape[1]
        self._dep_dims = training_values.shape[1]
        self._ntpts = training_points.shape[0]

        # Make training data into a Tree
        leavesz = ceil(self._ntpts / float(num_leaves))
        self._KData = cKDTree(self._tp, leafsize=leavesz)

        # Cache for gradients
        self._pt_cache = None
