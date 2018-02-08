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

# import itertools
# import unittest
#
# from numpy import array, linspace, sin, cos, pi

from sklearn.neural_network import MLPRegressor

from surrogate.estimator import ANNSurrogate

if __name__ == "__main__":
    X = [[0., 0.], [1., 1.], [10., 10.]]
    y = [0.0, 1.0, 10.0]
    x_pred = [[5., 5.], [-10., -2.]]

    surrogate = ANNSurrogate(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    surrogate.fit(X, y)
    y_pred = surrogate.predict(X)
    # print surrogate.regressor
    # print y_pred

    regressor = MLPRegressor(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    regressor.fit(X, y)
    y_pred = regressor.predict(X)
    print regressor
    print y_pred
