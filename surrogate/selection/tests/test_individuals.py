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

from surrogate.base import Individual


def Individuals(n=10):
    return [
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=10.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=9.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=8.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=7.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=6.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=5.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=4.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=3.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=2.0, constrain=[]),
        Individual(variable=[x / 10.0 for x in range(0, 10, 1)], fitness=1.0, constrain=[])
    ]
