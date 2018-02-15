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

"""Utilities for the SurrogateModel test process."""

from math import isnan

import numpy as np

def assert_rel_error(test_case, actual, desired, tolerance):
    """
    Determine that the relative error between `actual` and `desired`
    is within `tolerance`. If `desired` is zero, then use absolute error.

    Args
    ----
    test_case : :class:`unittest.TestCase`
        TestCase instance used for assertions.

    actual : float
        The value from the test.

    desired : float
        The value expected.

    tolerance : float
        Maximum relative error ``(actual - desired) / desired``.
    """
    try:
        actual[0]
    except (TypeError, IndexError):
        if isnan(actual) and not isnan(desired):
            test_case.fail('actual nan, desired %s, rel error nan, tolerance %s'
                           % (desired, tolerance))
        if desired != 0:
            error = (actual - desired) / desired
        else:
            error = actual
        if abs(error) > tolerance:
            test_case.fail('actual %s, desired %s, rel error %s, tolerance %s'
                           % (actual, desired, error, tolerance))
    else:  # array values
        if not np.all(np.isnan(actual) == np.isnan(desired)):
            test_case.fail('actual and desired values have non-matching nan values')

        if np.linalg.norm(desired) == 0:
            error = np.linalg.norm(actual)
        else:
            error = np.linalg.norm(actual - desired) / np.linalg.norm(desired)

        if abs(error) > tolerance:
            test_case.fail('arrays do not match, rel error %.3e > tol (%.3e)' % (error, tolerance))

    return error
