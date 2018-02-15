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

from collections import defaultdict

def sorNondominated(individuals, k, first_front_only=False):
    """Sort the first *k* *individuals* into different nondomination levels
    using the "Fast Nondominated Sorting Approach" proposed by Deb et al.,
    see [Deb2002]_. This algorithm has a time complexity of :math:`O(MN^2)`,
    where :math:`M` is the number of objectives and :math:`N` the number of
    individuals.

    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    :param first_front_only: If :obj:`True` sort only the first front and
                             exit.
    :returns: A list of Pareto fronts (lists), the first list includes
              nondominated individuals.

    .. [Deb2002] Deb, Pratab, Agarwal, and Meyarivan, "A fast elitist
       non-dominated sorting genetic algorithm for multi-objective
       optimization: NSGA-II", 2002.
    """
    if k == 0:
        return []

    map_fit_ind = defaultdict(list)
    for ind in individuals:
        map_fit_ind[ind.fitness].append(ind)
    fits = map_fit_ind.keys()

    current_front = []
    next_front = []
    dominating_fits = defaultdict(int)
    dominated_fits = defaultdict(list)

    # Rank first Pareto front
    for i, fit_i in enumerate(fits):
        for fit_j in fits[i + 1:]:
            if fit_i.dominates(fit_j):
                dominating_fits[fit_j] += 1
                dominated_fits[fit_i].append(fit_j)
            elif fit_j.dominates(fit_i):
                dominating_fits[fit_i] += 1
                dominated_fits[fit_j].append(fit_i)
        if dominating_fits[fit_i] == 0:
            current_front.append(fit_i)

    fronts = [[]]
    for fit in current_front:
        fronts[-1].extend(map_fit_ind[fit])
    pareto_sorted = len(fronts[-1])

    # Rank the next front until all individuals are sorted or
    # the given number of individual are sorted.
    if not first_front_only:
        N = min(len(individuals), k)
        while pareto_sorted < N:
            fronts.append([])
            for fit_p in current_front:
                for fit_d in dominated_fits[fit_p]:
                    dominating_fits[fit_d] -= 1
                    if dominating_fits[fit_d] == 0:
                        next_front.append(fit_d)
                        pareto_sorted += len(map_fit_ind[fit_d])
                        fronts[-1].extend(map_fit_ind[fit_d])
            current_front = next_front
            next_front = []

    return fronts
