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

"""
Base classes for all estimators.
Class definition for Individual, the base class for all surrogate models.
"""

import sys

from collections import Sequence
from operator import mul, truediv

class Individual(object):
    """A Individual

    :ref:`Fitness`

    :param estimator: physical based model
    """

    def __init__(self, estimator, variable=None, constraint=None, weights=()):
        """__init__

        :param estimator:
        :param variable:
        :param constraint:
        :param weights:
        :return:
        """
        # needed
        self.estimator = estimator

        if variable is None:
            self.variable = {}
        else:
            self.variable = variable

        # if objective is None:
        #     self.objective = {}
        # else:
        #     self.objective = objective

        if constraint is None:
            self.constraint = {}
        else:
            self.constraint = constraint

        # not yet decided
        self.fitness = Fitness(estimator(variable), weights)
        # self.rank = None
        # self.distance = None
        # self.strategy = set()
        # self.solution = set()
        # self.feature = None
        # self.dominate = None

        # deap
        # NDIM = 5
        # MU = 12
        # pop = toolbox.population(n=MU)
        #
        # # Evaluate the individuals with an invalid fitness
        # invalid_ind = [ind for ind in pop if not ind.fitness.valid]
        # fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        #
        # for ind, fit in zip(invalid_ind, fitnesses):
        #     ind.fitness.values = fit
        #
        # # debug
        # 10 = {individual} array('d', [0.87, 0.74, 0.16, 0.67, 0.42])
        #     .fitness
        #         .crowding_dist = {float} inf
        #         .valid = {bool} True
        #         .values = {tuple} (0.99, 8.46)
        #         .weights = {tuple} (-1.0, -1.0)
        #         .wvalues = {tuple} (-0.99, -8.46)
        #     .itemsize = {int} 8
        #     .typecode = {str} 'd'


    def getVar(self, i):
        """The fitness is a measure of quality of a solution. If *values* are
        provided as a tuple, the fitness is initalized using those values,
        otherwise it is empty (or invalid).

        :param i: index of variable

        .. code-block:: python

            if not (isinstance(i, int) and i >= 0):
                raise ValueError("Variable index must be an integer >= 0 .")

        .. note::
            Note
        """

        if not (isinstance(i, int) and i >= 0):
            raise ValueError("Variable index must be an integer >= 0 .")
        return self._variables[i]

    # def __len__(self):
    #     return len(self.variable)
    # def __repr__(self):
    #     return repr((self.variable, self.objective, self.constraint, self.fitness))


class Fitness(object):
    """The fitness is a measure of quality of a solution. If *values* are
    provided as a tuple, the fitness is initalized using those values,
    otherwise it is empty (or invalid).

    :param values: The initial values of the fitness as a tuple, optional.

    Fitnesses may be compared using the ``>``, ``<``, ``>=``, ``<=``, ``==``,
    ``!=``. The comparison of those operators is made lexicographically.
    Maximization and minimization are taken care off by a multiplication
    between the :attr:`weights` and the fitness :attr:`values`. The comparison
    can be made between fitnesses of different size, if the fitnesses are
    equal until the extra elements, the longer fitness will be superior to the
    shorter.

    Different types of fitnesses.

    .. note::
        When comparing fitness values that are **minimized**, ``a > b`` will
        return :data:`True` if *a* is **smaller** than *b*.
    """

    weights = None
    """
    The weights are used in the fitness comparison. They are shared among
    all fitnesses of the same type. When subclassing :class:`Fitness`, the
    weights must be defined as a tuple where each element is associated to an
    objective.
    A negative weight element corresponds to: (-1.0, -1.0)
    ``the minimization of the associated objective.``
    A positive weight element corresponds to: (1.0, 1.0)
    ``the maximization of the associated objective.``

    .. note::
        If weights is not defined during subclassing, the following error will
        occur at instantiation of a subclass fitness object:

        ``TypeError: Can't instantiate abstract <class Fitness[...]> with
        abstract attribute weights.``
    """

    wvalues = ()
    """Contains the weighted values of the fitness, the multiplication with the
    weights is made when the values are set via the property :attr:`values`.
    Multiplication is made on setting of the values for efficiency.

    Generally it is unnecessary to manipulate wvalues as it is an internal
    attribute of the fitness used in the comparison operators.
    """

    def __init__(self, values=(), weights=()):
        if weights is None:
            raise TypeError("Can't instantiate abstract %r with abstract "
                            "attribute weights." % (self.__class__))
        self.weights = weights
        if not isinstance(self.weights, Sequence):
            raise TypeError("Attribute weights of %r must be a sequence."
                            % self.__class__)

        if len(values) > 0:
            self.values = values

    def getValues(self):
        return tuple(map(truediv, self.wvalues, self.weights))

    def setValues(self, values):
        try:
            self.wvalues = tuple(map(mul, values, self.weights))
        except TypeError:
            _, _, traceback = sys.exc_info()
            raise TypeError, ("Both weights and assigned values must be a "
                              "sequence of numbers when assigning to values of "
                              "%r. Currently assigning value(s) %r of %r to a fitness with "
                              "weights %s."
                              % (self.__class__, values, type(values), self.weights)), traceback

    def delValues(self):
        self.wvalues = ()

    values = property(getValues, setValues, delValues,
                      ("Fitness values. Use directly ``individual.fitness.values = values`` "
                       "in order to set the fitness and ``del individual.fitness.values`` "
                       "in order to clear (invalidate) the fitness. The (unweighted) fitness "
                       "can be directly accessed via ``individual.fitness.values``."))

    def dominates(self, other, obj=slice(None)):
        """Return true if each objective of *self* is not strictly worse than
        the corresponding objective of *other* and at least one objective is
        strictly better.

        :param obj: Slice indicating on which objectives the domination is
                    tested. The default value is `slice(None)`, representing
                    every objectives.
        """

        not_equal = False
        for self_wvalue, other_wvalue in zip(self.wvalues[obj], other.wvalues[obj]):
            if self_wvalue > other_wvalue:
                not_equal = True
            elif self_wvalue < other_wvalue:
                return False
        return not_equal

    @property
    def valid(self):
        """Assess if a fitness is valid or not."""
        return len(self.wvalues) != 0

    def __hash__(self):
        """hash

        :return:
        """
        return hash(self.wvalues)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.wvalues <= other.wvalues

    def __lt__(self, other):
        return self.wvalues < other.wvalues

    def __eq__(self, other):
        return self.wvalues == other.wvalues

    def __ne__(self, other):
        return not self.__eq__(other)

    # TODO 20161212 pass memeory address instead of values
    # offspring = [deepcopy(ind) for ind in offspring]
    # def __deepcopy__(self, memo):
    #     """Replace the basic deepcopy function with a faster one.
    #
    #     It assumes that the elements in the :attr:`values` tuple are
    #     immutable and the fitness does not contain any other object
    #     than :attr:`values` and :attr:`weights`.
    #     """
    #     copy_ = self.__class__()
    #     copy_.wvalues = self.wvalues
    #     return copy_

    def __str__(self):
        """Return the values of the Fitness object."""
        return str(self.values if self.valid else tuple())

    def __repr__(self):
        """Return the Python code to build a copy of the object."""
        return "%s.%s(%r)" % (self.__module__, self.__class__.__name__,
                              self.values if self.valid else tuple())


class SurrogateModel(object):
    """A class for surrogate models.

    :ref:`Individual`
    """

    def __init__(self):
        self.trained = False

    def fit(self, x, y):
        """fit ML model

        :param x: training dataset
        :param y: training dataset
        :return: void
        """
        self.trained = True

    def predict(self, x):
        if not self.trained:
            msg = "{0} has not been trained, so no prediction can be made." \
                .format(type(self).__name__)
            raise RuntimeError(msg)

    def predict_proba(self, x):
        if not self.trained:
            msg = "{0} has not been trained, so no prediction can be made." \
                .format(type(self).__name__)
            raise RuntimeError(msg)
            # raise NotImplementedError('predict_proba not implemented.')

    def linearize(self, x):
        msg = "{0} has not defined a jacobian method." \
            .format(type(self).__name__)
        raise RuntimeError(msg)


class MultiFiSurrogateModel(SurrogateModel):
    """Base class for surrogate models using multi-fiddelity training data

    :param SurrogateModel: Object
    """

    def fit(self, x, y):
        """fit ML model

        :param x: training dataset
        :param y: training dataset
        :return: void
        """
        super(MultiFiSurrogateModel, self).train(x, y)
        self.train_multifi([x], [y])

    def train_multifi(self, x, y):
        """Trains the surrogate model, based on the given
        multi-fidelity training data.

        x: list of (m samples, n inputs) ndarrays
            Values representing the multi-fidelity training case inputs.
        y: list of ndarray
            output training values which corresponds to the multi-fidelity
            training case input given by x.
        """
