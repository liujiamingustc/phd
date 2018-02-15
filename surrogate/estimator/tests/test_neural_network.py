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
