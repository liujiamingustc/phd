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

def assignCrowdingDist(individuals):
    """Assign a crowding distance to each individual's fitness. The
    crowding distance can be retrieve via the :attr:`crowding_dist`
    attribute of each individual's fitness.
    """
    if len(individuals) == 0:
        return

    distances = [0.0] * len(individuals)
    crowd = [(ind.fitness.values, i) for i, ind in enumerate(individuals)]

    nobj = len(individuals[0].fitness.values)

    for i in xrange(nobj):
        crowd.sort(key=lambda element: element[0][i])
        distances[crowd[0][1]] = float("inf")
        distances[crowd[-1][1]] = float("inf")
        if crowd[-1][0][i] == crowd[0][0][i]:
            continue
        norm = nobj * float(crowd[-1][0][i] - crowd[0][0][i])
        for prev, cur, next in zip(crowd[:-2], crowd[1:-1], crowd[2:]):
            distances[cur[1]] += (next[0][i] - prev[0][i]) / norm

    for i, dist in enumerate(distances):
        individuals[i].fitness.crowding_dist = dist
