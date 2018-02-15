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

import math

from .utils import randomizedSelect

def selSPEA2(individuals, k):
    """Apply SPEA-II selection operator on the *individuals*. Usually, the
    size of *individuals* will be larger than *n* because any individual
    present in *individuals* will appear in the returned list at most once.
    Having the size of *individuals* equals to *n* will have no effect other
    than sorting the population according to a strength Pareto scheme. The
    list returned contains references to the input *individuals*. For more
    details on the SPEA-II operator see [Zitzler2001]_.

    :param individuals: A list of individuals to select from.
    :param k: The number of individuals to select.
    :returns: A list of selected individuals.

    .. [Zitzler2001] Zitzler, Laumanns and Thiele, "SPEA 2: Improving the
       strength Pareto evolutionary algorithm", 2001.
    """
    N = len(individuals)
    L = len(individuals[0].fitness.values)
    K = math.sqrt(N)
    strength_fits = [0] * N
    fits = [0] * N
    dominating_inds = [list() for i in xrange(N)]

    for i, ind_i in enumerate(individuals):
        for j, ind_j in enumerate(individuals[i + 1:], i + 1):
            if ind_i.fitness.dominates(ind_j.fitness):
                strength_fits[i] += 1
                dominating_inds[j].append(i)
            elif ind_j.fitness.dominates(ind_i.fitness):
                strength_fits[j] += 1
                dominating_inds[i].append(j)

    for i in xrange(N):
        for j in dominating_inds[i]:
            fits[i] += strength_fits[j]

    # Choose all non-dominated individuals
    chosen_indices = [i for i in xrange(N) if fits[i] < 1]

    if len(chosen_indices) < k:  # The archive is too small
        for i in xrange(N):
            distances = [0.0] * N
            for j in xrange(i + 1, N):
                dist = 0.0
                for l in xrange(L):
                    val = individuals[i].fitness.values[l] - \
                          individuals[j].fitness.values[l]
                    dist += val * val
                distances[j] = dist
            kth_dist = randomizedSelect(distances, 0, N - 1, K)
            density = 1.0 / (kth_dist + 2.0)
            fits[i] += density

        next_indices = [(fits[i], i) for i in xrange(N)
                        if not i in chosen_indices]
        next_indices.sort()
        # print next_indices
        chosen_indices += [i for _, i in next_indices[:k - len(chosen_indices)]]

    elif len(chosen_indices) > k:  # The archive is too large
        N = len(chosen_indices)
        distances = [[0.0] * N for i in xrange(N)]
        sorted_indices = [[0] * N for i in xrange(N)]
        for i in xrange(N):
            for j in xrange(i + 1, N):
                dist = 0.0
                for l in xrange(L):
                    val = individuals[chosen_indices[i]].fitness.values[l] - \
                          individuals[chosen_indices[j]].fitness.values[l]
                    dist += val * val
                distances[i][j] = dist
                distances[j][i] = dist
            distances[i][i] = -1

        # Insert sort is faster than quick sort for short arrays
        for i in xrange(N):
            for j in xrange(1, N):
                l = j
                while l > 0 and distances[i][j] < distances[i][sorted_indices[i][l - 1]]:
                    sorted_indices[i][l] = sorted_indices[i][l - 1]
                    l -= 1
                sorted_indices[i][l] = j

        size = N
        to_remove = []
        while size > k:
            # Search for minimal distance
            min_pos = 0
            for i in xrange(1, N):
                for j in xrange(1, size):
                    dist_i_sorted_j = distances[i][sorted_indices[i][j]]
                    dist_min_sorted_j = distances[min_pos][sorted_indices[min_pos][j]]

                    if dist_i_sorted_j < dist_min_sorted_j:
                        min_pos = i
                        break
                    elif dist_i_sorted_j > dist_min_sorted_j:
                        break

            # Remove minimal distance from sorted_indices
            for i in xrange(N):
                distances[i][min_pos] = float("inf")
                distances[min_pos][i] = float("inf")

                for j in xrange(1, size - 1):
                    if sorted_indices[i][j] == min_pos:
                        sorted_indices[i][j] = sorted_indices[i][j + 1]
                        sorted_indices[i][j + 1] = min_pos

            # Remove corresponding individual from chosen_indices
            to_remove.append(min_pos)
            size -= 1

        for index in reversed(sorted(to_remove)):
            del chosen_indices[index]

    return [individuals[i] for i in chosen_indices]
