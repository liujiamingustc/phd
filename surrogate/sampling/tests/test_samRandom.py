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

from surrogate.sampling import *

print '\nTest sampling.samRandom: samRandom'
n = 3
print samRandom(n)

print '\nTest sampling.samRandom: samBeta'
a, b, size = 0.1, 0.5, 10
print samBeta(a, b, size)

print '\nTest sampling.samRandom: samBinomial'
n, p, size = 10, 0.5, 10
print samBinomial(n, p, size)

print '\nTest sampling.samRandom: samChiSquare'
df, size = 2, 10
print samChiSquare(df, size)

print '\nTest sampling.samRandom: samExponential'
scale, size = 0.2, 10
print samExponential(scale, size)

print '\nTest sampling.samRandom: samF'
dfnum, dfden, size = 1, 48, 10
print samF(dfnum, dfden, size)

print '\nTest sampling.samRandom: samGamma'
shape, scale, size = 2.0, 2.0, 10
print samGamma(shape, scale, size)

print '\nTest sampling.samRandom: samGumbel'
# mu, beta = 0, 0.1
loc, scale, size = 0, 0.1, 10
print samGumbel(loc, scale, size)

print '\nTest sampling.samRandom: samLaplace'
loc, scale, size = 0.0, 1.0, 10
print samLaplace(loc, scale, size)

print '\nTest sampling.samRandom: samLogistic'
loc, scale, size = 10, 1, 10
print samLogistic(loc, scale, size)

print '\nTest sampling.samRandom: samLognormal'
mean, sigma, size = 3.0, 1.0, 10
print samLognormal(mean, sigma, size)

print '\nTest sampling.samRandom: samNormal'
# mu, sigma = 0, 0.1
loc, scale, size = 0, 0.1, 10
print samNormal(loc, scale, size)

print '\nTest sampling.samRandom: samPareto'
a, size = 3.0, 10
print samPareto(a, size)

print '\nTest sampling.samRandom: samPoisson'
lam, size = 3.0, 10
print samPoisson(lam, size)

print '\nTest sampling.samRandom: samPower'
a, size = 3.0, 10
print samPower(a, size)

print '\nTest sampling.samRandom: samRayleigh'
scale, size = 3.0, 10
print samRayleigh(scale, size)

print '\nTest sampling.samRandom: samTriangular'
left, mode, right, size = -3, 0, 8, 10
print samTriangular(left, mode, right, size)

print '\nTest sampling.samRandom: samUniform'
low, high, size = 0.0, 1.0, 10
print samUniform(low, high, size)

print '\nTest sampling.samRandom: samVonmises'
mu, kappa, size = 0.0, 4.0, 10
print samVonmises(mu, kappa, size)

print '\nTest sampling.samRandom: samWald'
mean, scale, size = 3, 2, 10
print samWald(mean, scale, size)

print '\nTest sampling.samRandom: samWeibull'
a, size = 5.0, 10
print samWeibull(a, size)

print '\nTest sampling.samRandom: samZipf'
a, size = 2.0, 10
print samZipf(a, size)

