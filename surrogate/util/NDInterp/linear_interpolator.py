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

from surrogate.util.NDInterp.nn_base import NNBase

class LinearInterpolator(NNBase):
    """
    Interpolates values by forming a hyperplane between the points closest to
    the prescribed inputs.
    """

    def _find_hyperplane(self, nloc):
        # Extra Inputs for Finding the normal are found below
        # Number of row vectors needed always dimensions - 1
        indep_dims = self._indep_dims
        dep_dims = self._dep_dims

        # Number of Prediction Points
        nppts = nloc.shape[0]

        # Preallocate storage
        pc = np.empty((nppts, dep_dims), dtype='float')
        normal = np.empty((nppts, indep_dims + 1, dep_dims), dtype='float')
        nvect = np.empty((nppts, indep_dims, indep_dims + 1), dtype='float')
        trnd = np.concatenate((self._tp[nloc, :],
                               self._tv[nloc, 0].reshape(nppts, indep_dims + 1, 1)),
                              axis=2)
        nvect[:, :, :-1] = trnd[:, 1:, :-1] - trnd[:, :-1, :-1]

        for i in xrange(dep_dims):
            # Planar vectors need both dep and ind dimensions
            trnd[:, :, -1] = self._tv[nloc, i]

            # Go through each neighbor
            # Creates array[neighbor, dimension] from NN results
            nvect[:, :, -1] = trnd[:, 1:, -1] - trnd[:, :-1, -1]

            # Normal vector is in the null space of nvect.
            # Since nvect is of size indep x (indep + 1),
            # the normal vector will be the last entry in
            # V in the U, Sigma, V = svd(nvect).
            normal[:, :, i] = np.linalg.svd(nvect)[2][:, -1, :]

            # Use the point of the closest neighbor to
            # solve for pc - the constant of the n-dimensional plane.
            pc[:, i] = np.einsum('ij,ij->i', trnd[:, 0, :], normal[:, :, i])

        return normal, pc

    def __call__(self, prediction_points):
        # This method uses linear interpolation by defining a plane with
        # a set number of nearest neighbors to the predicted

        if len(prediction_points.shape) == 1:
            # Reshape vector to n x 1 array
            prediction_points.shape = (1, prediction_points.shape[0])

        normalized_pts = (prediction_points - self._tpm) / self._tpr

        # Linear interp only uses as many neighbors as it has dimensions
        points_needed = self._indep_dims + 1

        # KData query takes (data, #ofneighbors) to determine closest
        # training points to predicted data
        ndist, nloc = self._KData.query(normalized_pts.real, points_needed)

        normal, pc = self._find_hyperplane(nloc)

        # Set all predictions from values on plane
        predictions = np.einsum('ij,ijk->ik', normalized_pts,
                                normal[:, :self._indep_dims, :]) - pc

        # Check to see if there are any collinear points and replace them
        n0 = np.where(normal[:, -1, :] == 0)
        predictions[n0, :] = self._tv[nloc[0, n0], :]

        # Finish computation for the good normals
        n = np.where(normal[:, -1, :] != 0)
        predictions[n] /= -normal[:, -1, :][n]

        # Rescale to original units
        predictions = (predictions * self._tvr) + self._tvm

        self._pt_cache = (normalized_pts, ndist, nloc)

        return predictions

    def gradient(self, PredPoints):
        # Extra method to find the gradient at each location of a set of
        # supplied predicted points.

        if len(PredPoints.shape) == 1:
            # Reshape vector to n x 1 array
            PredPoints.shape = (1, PredPoints.shape[0])

        normPredPts = (PredPoints - self._tpm) / self._tpr
        nppts = normPredPts.shape[0]
        gradient = np.zeros((nppts, self._dep_dims, self._indep_dims), dtype="float")
        # Linear interp only uses as many neighbors as it has dimensions
        dims = self._indep_dims + 1
        # Find the neighbors
        if self._pt_cache is not None and \
                np.allclose(self._pt_cache[0], normPredPts):
            ndist, nloc = self._pt_cache[1:]
        else:
            ndist, nloc = self._KData.query(normPredPts.real, dims)

        normal, pc = self._find_hyperplane(nloc)
        if np.any(normal[:, -1, :]) == 0:
            return gradient
        gradient[:] = (-normal[:, :-1, :] / normal[:, -1, :]).squeeze().T

        grad = gradient * (self._tvr[:, np.newaxis] / self._tpr)
        return grad
