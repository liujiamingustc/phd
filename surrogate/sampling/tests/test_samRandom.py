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

