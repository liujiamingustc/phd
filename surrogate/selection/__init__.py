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

from .selBest import selBest
from .selDoubleTournament import selDoubleTournament
from .selNSGA2 import selNSGA2
from .selRandom import selRandom
from .selRoulette import selRoulette
from .selSPEA2 import selSPEA2
from .selStochasticUniversalSampling import selStochasticUniversalSampling
from .selTournament import selTournament
from .selTournamentDCD import selTournamentDCD
from .selWorst import selWorst

__all__ = [
    'selRandom',
    'selBest', 'selWorst',
    'selTournament', 'selDoubleTournament', 'selTournamentDCD',
    'selStochasticUniversalSampling',
    'selRoulette',
    'selNSGA2', 'selSPEA2'
]
