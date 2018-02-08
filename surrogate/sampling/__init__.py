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

"""Sampling Strategy, Experimental Design

MOEA selection strategy:
    1.Random sampling
    2.Best sampling
    3.Tournament sampling
    4.Tournament+Best sampling

Links:
    https://www.google.nl/search?sclient=psy-ab&client=safari&rls=en&q=github+sampling+python&oq=github+sampling+python&gs_l=serp.3..0i22i30k1l2.2824.3846.0.4517.7.7.0.0.0.0.91.551.7.7.0....0...1c.1.64.psy-ab..0.7.538...33i160k1.G42G3jxX1XY&pbx=1&biw=1680&bih=961&dpr=2&cad=cbv&bvch=u&sei=-e5HWNLGHsrNgAbDjruoAg#q=github+sampling+strategy+python

    https://en.wikipedia.org/wiki/Sampling_(statistics)

    https://en.wikipedia.org/wiki/Latin_hypercube_sampling

    https://docs.scipy.org/doc/numpy/reference/routines.random.html

    Factorial Designs:
        samFullFact, samFracFact, samFF2n, samPlackettBurman
    Response-Surface Designs:
        samBoxBehnken, samCentralComposite
    Randomized Designs:
        samLatinHypercube
"""

from .samBoxBehnken import samBoxBehnken
from .samCentralComposite import samCentralComposite
from .samFullFact import samFullFact, samFracFact, samFF2n
from .samLatinHypercube import samLatinHypercube
from .samOptimalLHC import samOptimalLHC
from .samPlackettBurman import samPlackettBurman
from .samRandom import samRandom, samBeta, samBinomial, samChiSquare, \
    samExponential, samF, samGamma, samGumbel, \
    samLaplace, samLogistic, samLognormal, samNormal, \
    samPareto, samPoisson, samPower, samRayleigh, \
    samTriangular, samUniform, samVonmises, samWald, \
    samWeibull, samZipf
from .samRandomLHC import samRandomLHC

__all__ = [
    'samRandomLHC', 'samOptimalLHC',
    'samFullFact', 'samFracFact', 'samFF2n', 'samPlackettBurman',
    'samBoxBehnken', 'samCentralComposite',
    'samLatinHypercube',
    'samRandom', 'samBeta', 'samBinomial', 'samChiSquare',
    'samExponential', 'samF', 'samGamma', 'samGumbel',
    'samLaplace', 'samLogistic', 'samLognormal', 'samNormal',
    'samPareto', 'samPoisson', 'samPower', 'samRayleigh',
    'samTriangular', 'samUniform', 'samVonmises', 'samWald',
    'samWeibull', 'samZipf'
]
