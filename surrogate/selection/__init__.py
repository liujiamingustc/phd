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
