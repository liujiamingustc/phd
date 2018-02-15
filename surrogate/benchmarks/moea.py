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

# This file is part of DEAP.
#
# DEAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# DEAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

"""
Regroup typical EC benchmarks functions to import easily and benchmark
examples.
"""

from functools import reduce
from math import sin, cos, pi, exp, e, sqrt
from operator import mul

import numpy as np


# Unimodal
def rand(variable):
    """Random test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization or maximization
       * - Range
         - none
       * - Global optima
         - none
       * - Function
         - :math:`f(\mathbf{x}) = \\text{\\texttt{random}}(0,1)`
    """
    return np.random.random(),


def plane(variable):
    """Plane test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - none
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\mathbf{x}) = x_0`
    """
    return variable[0],


def sphere(variable):
    """Sphere test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - none
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\mathbf{x}) = \sum_{i=1}^Nx_i^2`
    """
    return sum(gene * gene for gene in variable),


def cigar(variable):
    """Cigar test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - none
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\mathbf{x}) = x_0^2 + 10^6\\sum_{i=1}^N\,x_i^2`
    """
    return variable[0] ** 2 + 1e6 * sum(gene * gene for gene in variable),


def rosenbrock(variable):
    """Rosenbrock test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - none
       * - Global optima
         - :math:`x_i = 1, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\\mathbf{x}) = \\sum_{i=1}^{N-1} (1-x_i)^2 + 100 (x_{i+1} - x_i^2 )^2`

    .. plot:: code/benchmarks/rosenbrock.py
       :width: 67 %
    """
    return sum(100 * (x * x - y) ** 2 + (1. - x) ** 2 \
               for x, y in zip(variable[:-1], variable[1:])),


def h1(variable):
    """ Simple two-dimensional function containing several local maxima.
    From: The Merits of a Parallel Genetic Algorithm in Solving Hard
    Optimization Problems, A. J. Knoek van Soest and L. J. R. Richard
    Casius, J. Biomech. Eng. 125, 141 (2003)

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - maximization
       * - Range
         - :math:`x_i \in [-100, 100]`
       * - Global optima
         - :math:`\mathbf{x} = (8.6998, 6.7665)`, :math:`f(\mathbf{x}) = 2`\n
       * - Function
         - :math:`f(\mathbf{x}) = \\frac{\sin(x_1 - \\frac{x_2}{8})^2 + \
            \\sin(x_2 + \\frac{x_1}{8})^2}{\\sqrt{(x_1 - 8.6998)^2 + \
            (x_2 - 6.7665)^2} + 1}`

    .. plot:: code/benchmarks/h1.py
       :width: 67 %
    """
    num = (sin(variable[0] - variable[1] / 8)) ** 2 + (sin(variable[1] + variable[0] / 8)) ** 2
    denum = ((variable[0] - 8.6998) ** 2 + (variable[1] - 6.7665) ** 2) ** 0.5 + 1
    return num / denum,

    #


# Multimodal
def ackley(variable):
    """Ackley test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-15, 30]`
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\\mathbf{x}) = 20 - 20\exp\left(-0.2\sqrt{\\frac{1}{N} \
            \\sum_{i=1}^N x_i^2} \\right) + e - \\exp\\left(\\frac{1}{N}\sum_{i=1}^N \\cos(2\pi x_i) \\right)`

    .. plot:: code/benchmarks/ackley.py
       :width: 67 %
    """
    N = len(variable)
    algha = 20
    beta = 0.2

    return algha - algha * exp(-beta * sqrt(1.0 / N * sum(x ** 2 for x in variable))) \
           + e - exp(1.0 / N * sum(cos(2 * pi * x) for x in variable)),


def bohachevsky(variable):
    """Bohachevsky test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-100, 100]`
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         -  :math:`f(\mathbf{x}) = \sum_{i=1}^{N-1}(x_i^2 + 2x_{i+1}^2 - \
                   0.3\cos(3\pi x_i) - 0.4\cos(4\pi x_{i+1}) + 0.7)`

    .. plot:: code/benchmarks/bohachevsky.py
       :width: 67 %
    """
    return sum(x ** 2 + 2 * x1 ** 2 - 0.3 * cos(3 * pi * x) - 0.4 * cos(4 * pi * x1) + 0.7
               for x, x1 in zip(variable[:-1], variable[1:])),


def griewank(variable):
    """Griewank test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-600, 600]`
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\\mathbf{x}) = \\frac{1}{4000}\\sum_{i=1}^N\,x_i^2 - \
                  \prod_{i=1}^N\\cos\\left(\\frac{x_i}{\sqrt{i}}\\right) + 1`

    .. plot:: code/benchmarks/griewank.py
       :width: 67 %
    """
    return 1.0 / 4000.0 * sum(x ** 2 for x in variable) - \
           reduce(mul, (cos(x / sqrt(i + 1.0)) for i, x in enumerate(variable)), 1) + 1,


def rastrigin(variable):
    """Rastrigin test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-5.12, 5.12]`
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\\mathbf{x}) = 10N \sum_{i=1}^N x_i^2 - 10 \\cos(2\\pi x_i)`

    .. plot:: code/benchmarks/rastrigin.py
       :width: 67 %
    """
    return 10 * len(variable) + sum(gene * gene - 10 * \
                                    cos(2 * pi * gene) for gene in variable),


def rastrigin_scaled(variable):
    """Scaled Rastrigin test objective function.

    :math:`f_{\\text{RastScaled}}(\mathbf{x}) = 10N + \sum_{i=1}^N \
        \left(10^{\left(\\frac{i-1}{N-1}\\right)} x_i \\right)^2 x_i)^2 - \
        10\cos\\left(2\\pi 10^{\left(\\frac{i-1}{N-1}\\right)} x_i \\right)`
    """
    N = len(variable)
    return 10 * N + sum((10 ** (i / (N - 1)) * x) ** 2 -
                        10 * cos(2 * pi * 10 ** (i / (N - 1)) * x) for i, x in enumerate(variable)),


def rastrigin_skew(variable):
    """Skewed Rastrigin test objective function.

     :math:`f_{\\text{RastSkew}}(\mathbf{x}) = 10N \sum_{i=1}^N \left(y_i^2 - 10 \\cos(2\\pi x_i)\\right)`

     :math:`\\text{with } y_i = \
                            \\begin{cases} \
                                10\\cdot x_i & \\text{ if } x_i > 0,\\\ \
                                x_i & \\text{ otherwise } \
                            \\end{cases}`
    """
    N = len(variable)
    return 10 * N + sum((10 * x if x > 0 else x) ** 2
                        - 10 * cos(2 * pi * (10 * x if x > 0 else x)) for x in variable),


def schaffer(variable):
    """Schaffer test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-100, 100]`
       * - Global optima
         - :math:`x_i = 0, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         -  :math:`f(\mathbf{x}) = \sum_{i=1}^{N-1} (x_i^2+x_{i+1}^2)^{0.25} \cdot \
                  \\left[ \sin^2(50\cdot(x_i^2+x_{i+1}^2)^{0.10}) + 1.0 \
                  \\right]`

    .. plot:: code/benchmarks/schaffer.py
        :width: 67 %
    """
    return sum((x ** 2 + x1 ** 2) ** 0.25 * ((sin(50 * (x ** 2 + x1 ** 2) ** 0.1)) ** 2 + 1.0)
               for x, x1 in zip(variable[:-1], variable[1:])),


def schwefel(variable):
    """Schwefel test objective function.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-500, 500]`
       * - Global optima
         - :math:`x_i = 420.96874636, \\forall i \in \\lbrace 1 \\ldots N\\rbrace`, :math:`f(\mathbf{x}) = 0`
       * - Function
         - :math:`f(\mathbf{x}) = 418.9828872724339\cdot N - \
            \sum_{i=1}^N\,x_i\sin\\left(\sqrt{|x_i|}\\right)`


    .. plot:: code/benchmarks/schwefel.py
        :width: 67 %
    """
    N = len(variable)
    return 418.9828872724339 * N - sum(x * sin(sqrt(abs(x))) for x in variable),


def himmelblau(variable):
    """The Himmelblau's function is multimodal with 4 defined minimums in
    :math:`[-6, 6]^2`.

    .. list-table::
       :widths: 10 50
       :stub-columns: 1

       * - Type
         - minimization
       * - Range
         - :math:`x_i \in [-6, 6]`
       * - Global optima
         - :math:`\mathbf{x}_1 = (3.0, 2.0)`, :math:`f(\mathbf{x}_1) = 0`\n
           :math:`\mathbf{x}_2 = (-2.805118, 3.131312)`, :math:`f(\mathbf{x}_2) = 0`\n
           :math:`\mathbf{x}_3 = (-3.779310, -3.283186)`, :math:`f(\mathbf{x}_3) = 0`\n
           :math:`\mathbf{x}_4 = (3.584428, -1.848126)`, :math:`f(\mathbf{x}_4) = 0`\n
       * - Function
         - :math:`f(x_1, x_2) = (x_1^2 + x_2 - 11)^2 + (x_1 + x_2^2 -7)^2`

    .. plot:: code/benchmarks/himmelblau.py
        :width: 67 %
    """
    return (variable[0] * variable[0] + variable[1] - 11) ** 2 + \
           (variable[0] + variable[1] * variable[1] - 7) ** 2,


def shekel(variable, a, c):
    """The Shekel multimodal function can have any number of maxima. The number
    of maxima is given by the length of any of the arguments *a* or *c*, *a*
    is a matrix of size :math:`M\\times N`, where *M* is the number of maxima
    and *N* the number of dimensions and *c* is a :math:`M\\times 1` vector.
    The matrix :math:`\\mathcal{A}` can be seen as the position of the maxima
    and the vector :math:`\\mathbf{c}`, the width of the maxima.

    :math:`f_\\text{Shekel}(\mathbf{x}) = \\sum_{i = 1}^{M} \\frac{1}{c_{i} +
    \\sum_{j = 1}^{N} (x_{j} - a_{ij})^2 }`

    The following figure uses

    :math:`\\mathcal{A} = \\begin{bmatrix} 0.5 & 0.5 \\\\ 0.25 & 0.25 \\\\
    0.25 & 0.75 \\\\ 0.75 & 0.25 \\\\ 0.75 & 0.75 \\end{bmatrix}` and
    :math:`\\mathbf{c} = \\begin{bmatrix} 0.002 \\\\ 0.005 \\\\ 0.005
    \\\\ 0.005 \\\\ 0.005 \\end{bmatrix}`, thus defining 5 maximums in
    :math:`\\mathbb{R}^2`.

    .. plot:: code/benchmarks/shekel.py
        :width: 67 %
    """
    return sum((1. / (c[i] + sum((x - a[i][j]) ** 2 for j, x in enumerate(variable)))) for i in range(len(c))),


# Multiobjectives
def kursawe(variable):
    """Kursawe multiobjective function.

    :math:`f_{\\text{Kursawe}1}(\\mathbf{x}) = \\sum_{i=1}^{N-1} -10 e^{-0.2 \\sqrt{x_i^2 + x_{i+1}^2} }`

    :math:`f_{\\text{Kursawe}2}(\\mathbf{x}) = \\sum_{i=1}^{N} |x_i|^{0.8} + 5 \\sin(x_i^3)`

    .. plot:: code/benchmarks/kursawe.py
       :width: 100 %
    """
    f1 = sum(-10 * exp(-0.2 * sqrt(x * x + y * y)) for x, y in zip(variable[:-1], variable[1:]))
    f2 = sum(abs(x) ** 0.8 + 5 * sin(x * x * x) for x in variable)
    return np.array([f1, f2]).tolist()


def schaffer_mo(variable):
    """Schaffer's multiobjective function on a one attribute *variable*.
    From: J. D. Schaffer, "Multiple objective optimization with vector
    evaluated genetic algorithms", in Proceedings of the First International
    Conference on Genetic Algorithms, 1987.

    :math:`f_{\\text{Schaffer}1}(\\mathbf{x}) = x_1^2`

    :math:`f_{\\text{Schaffer}2}(\\mathbf{x}) = (x_1-2)^2`
    """
    f1 = variable[0] ** 2
    f2 = (variable[0] - 2) ** 2
    return np.array([f1, f2]).tolist()


def zdt1(variable):
    """ZDT1 multiobjective function.

    :math:`g(\\mathbf{x}) = 1 + \\frac{9}{n-1}\\sum_{i=2}^n x_i`

    :math:`f_{\\text{ZDT1}1}(\\mathbf{x}) = x_1`

    :math:`f_{\\text{ZDT1}2}(\\mathbf{x}) = g(\\mathbf{x})\\left[1 - \\sqrt{\\frac{x_1}{g(\\mathbf{x})}}\\right]`
    """
    g = 1.0 + 9.0 * sum(variable[1:]) / (len(variable) - 1)
    f1 = variable[0]
    f2 = g * (1 - sqrt(f1 / g))
    return np.array([f1, f2]).tolist()


def zdt2(variable):
    """ZDT2 multiobjective function.

    :math:`g(\\mathbf{x}) = 1 + \\frac{9}{n-1}\\sum_{i=2}^n x_i`

    :math:`f_{\\text{ZDT2}1}(\\mathbf{x}) = x_1`

    :math:`f_{\\text{ZDT2}2}(\\mathbf{x}) = g(\\mathbf{x})\\left[1 - \\left(\\frac{x_1}{g(\\mathbf{x})}\\right)^2\\right]`

    """

    g = 1.0 + 9.0 * sum(variable[1:]) / (len(variable) - 1)
    f1 = variable[0]
    f2 = g * (1 - (f1 / g) ** 2)
    return np.array([f1, f2]).tolist()


def zdt3(variable):
    """ZDT3 multiobjective function.

    :math:`g(\\mathbf{x}) = 1 + \\frac{9}{n-1}\\sum_{i=2}^n x_i`

    :math:`f_{\\text{ZDT3}1}(\\mathbf{x}) = x_1`

    :math:`f_{\\text{ZDT3}2}(\\mathbf{x}) = g(\\mathbf{x})\\left[1 - \\sqrt{\\frac{x_1}{g(\\mathbf{x})}} - \\frac{x_1}{g(\\mathbf{x})}\\sin(10\\pi x_1)\\right]`

    """

    g = 1.0 + 9.0 * sum(variable[1:]) / (len(variable) - 1)
    f1 = variable[0]
    f2 = g * (1 - sqrt(f1 / g) - f1 / g * sin(10 * pi * f1))
    return np.array([f1, f2]).tolist()


def zdt4(variable):
    """ZDT4 multiobjective function.

    :math:`g(\\mathbf{x}) = 1 + 10(n-1) + \\sum_{i=2}^n \\left[ x_i^2 - 10\\cos(4\\pi x_i) \\right]`

    :math:`f_{\\text{ZDT4}1}(\\mathbf{x}) = x_1`

    :math:`f_{\\text{ZDT4}2}(\\mathbf{x}) = g(\\mathbf{x})\\left[ 1 - \\sqrt{x_1/g(\\mathbf{x})} \\right]`

    """
    g = 1 + 10 * (len(variable) - 1) + sum(xi ** 2 - 10 * cos(4 * pi * xi) for xi in variable[1:])
    f1 = variable[0]
    f2 = g * (1 - sqrt(f1 / g))
    return np.array([f1, f2]).tolist()


def zdt6(variable):
    """ZDT6 multiobjective function.

    :math:`g(\\mathbf{x}) = 1 + 9 \\left[ \\left(\\sum_{i=2}^n x_i\\right)/(n-1) \\right]^{0.25}`

    :math:`f_{\\text{ZDT6}1}(\\mathbf{x}) = 1 - \\exp(-4x_1)\\sin^6(6\\pi x_1)`

    :math:`f_{\\text{ZDT6}2}(\\mathbf{x}) = g(\\mathbf{x}) \left[ 1 - (f_{\\text{ZDT6}1}(\\mathbf{x})/g(\\mathbf{x}))^2 \\right]`

    """
    g = 1 + 9 * (sum(variable[1:]) / (len(variable) - 1)) ** 0.25
    f1 = 1 - exp(-4 * variable[0]) * sin(6 * pi * variable[0]) ** 6
    f2 = g * (1 - (f1 / g) ** 2)
    return np.array([f1, f2]).tolist()


def dtlz1(variable, obj):
    """DTLZ1 mutliobjective function. It returns a tuple of *obj* values.
    The variable must have at least *obj* elements.
    From: K. Deb, L. Thiele, M. Laumanns and E. Zitzler. Scalable Multi-Objective
    Optimization Test Problems. CEC 2002, p. 825 - 830, IEEE Press, 2002.

    :math:`g(\\mathbf{x}_m) = 100\\left(|\\mathbf{x}_m| + \sum_{x_i \in \\mathbf{x}_m}\\left((x_i - 0.5)^2 - \\cos(20\pi(x_i - 0.5))\\right)\\right)`

    :math:`f_{\\text{DTLZ1}1}(\\mathbf{x}) = \\frac{1}{2} (1 + g(\\mathbf{x}_m)) \\prod_{i=1}^{m-1}x_i`

    :math:`f_{\\text{DTLZ1}2}(\\mathbf{x}) = \\frac{1}{2} (1 + g(\\mathbf{x}_m)) (1-x_{m-1}) \\prod_{i=1}^{m-2}x_i`

    :math:`\\ldots`

    :math:`f_{\\text{DTLZ1}m-1}(\\mathbf{x}) = \\frac{1}{2} (1 + g(\\mathbf{x}_m)) (1 - x_2) x_1`

    :math:`f_{\\text{DTLZ1}m}(\\mathbf{x}) = \\frac{1}{2} (1 - x_1)(1 + g(\\mathbf{x}_m))`

    Where :math:`m` is the number of objectives and :math:`\\mathbf{x}_m` is a
    vector of the remaining attributes :math:`[x_m~\\ldots~x_n]` of the
    variable in :math:`n > m` dimensions.

    """
    g = 100 * (
        len(variable[obj - 1:]) + sum((xi - 0.5) ** 2 - cos(20 * pi * (xi - 0.5)) for xi in variable[obj - 1:]))
    f = [0.5 * reduce(mul, variable[:obj - 1], 1) * (1 + g)]
    f.extend(0.5 * reduce(mul, variable[:m], 1) * (1 - variable[m]) * (1 + g) for m in reversed(xrange(obj - 1)))
    return f


def dtlz2(variable, obj):
    """DTLZ2 mutliobjective function. It returns a tuple of *obj* values.
    The variable must have at least *obj* elements.
    From: K. Deb, L. Thiele, M. Laumanns and E. Zitzler. Scalable Multi-Objective
    Optimization Test Problems. CEC 2002, p. 825 - 830, IEEE Press, 2002.

    :math:`g(\\mathbf{x}_m) = \\sum_{x_i \in \\mathbf{x}_m} (x_i - 0.5)^2`

    :math:`f_{\\text{DTLZ2}1}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\prod_{i=1}^{m-1} \\cos(0.5x_i\pi)`

    :math:`f_{\\text{DTLZ2}2}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{m-1}\pi ) \\prod_{i=1}^{m-2} \\cos(0.5x_i\pi)`

    :math:`\\ldots`

    :math:`f_{\\text{DTLZ2}m}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{1}\pi )`

    Where :math:`m` is the number of objectives and :math:`\\mathbf{x}_m` is a
    vector of the remaining attributes :math:`[x_m~\\ldots~x_n]` of the
    variable in :math:`n > m` dimensions.
    """
    xc = variable[:obj - 1]
    xm = variable[obj - 1:]
    g = sum((xi - 0.5) ** 2 for xi in xm)
    f = [(1.0 + g) * reduce(mul, (cos(0.5 * xi * pi) for xi in xc), 1.0)]
    f.extend((1.0 + g) * reduce(mul, (cos(0.5 * xi * pi) for xi in xc[:m]), 1) * sin(0.5 * xc[m] * pi) for m in
             range(obj - 2, -1, -1))

    return f


def dtlz3(variable, obj):
    """DTLZ3 mutliobjective function. It returns a tuple of *obj* values.
    The variable must have at least *obj* elements.
    From: K. Deb, L. Thiele, M. Laumanns and E. Zitzler. Scalable Multi-Objective
    Optimization Test Problems. CEC 2002, p. 825 - 830, IEEE Press, 2002.

    :math:`g(\\mathbf{x}_m) = 100\\left(|\\mathbf{x}_m| + \sum_{x_i \in \\mathbf{x}_m}\\left((x_i - 0.5)^2 - \\cos(20\pi(x_i - 0.5))\\right)\\right)`

    :math:`f_{\\text{DTLZ3}1}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\prod_{i=1}^{m-1} \\cos(0.5x_i\pi)`

    :math:`f_{\\text{DTLZ3}2}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{m-1}\pi ) \\prod_{i=1}^{m-2} \\cos(0.5x_i\pi)`

    :math:`\\ldots`

    :math:`f_{\\text{DTLZ3}m}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{1}\pi )`

    Where :math:`m` is the number of objectives and :math:`\\mathbf{x}_m` is a
    vector of the remaining attributes :math:`[x_m~\\ldots~x_n]` of the
    variable in :math:`n > m` dimensions.
    """
    xc = variable[:obj - 1]
    xm = variable[obj - 1:]
    g = 100 * (len(xm) + sum((xi - 0.5) ** 2 - cos(20 * pi * (xi - 0.5)) for xi in xm))
    f = [(1.0 + g) * reduce(mul, (cos(0.5 * xi * pi) for xi in xc), 1.0)]
    f.extend((1.0 + g) * reduce(mul, (cos(0.5 * xi * pi) for xi in xc[:m]), 1) * sin(0.5 * xc[m] * pi) for m in
             range(obj - 2, -1, -1))
    return f


def dtlz4(variable, obj, alpha):
    """DTLZ4 mutliobjective function. It returns a tuple of *obj* values. The
    variable must have at least *obj* elements. The *alpha* parameter allows
    for a meta-variable mapping in :func:`dtlz2` :math:`x_i \\rightarrow
    x_i^\\alpha`, the authors suggest :math:`\\alpha = 100`.
    From: K. Deb, L. Thiele, M. Laumanns and E. Zitzler. Scalable Multi-Objective
    Optimization Test Problems. CEC 2002, p. 825 - 830, IEEE Press, 2002.

    :math:`g(\\mathbf{x}_m) = \\sum_{x_i \in \\mathbf{x}_m} (x_i - 0.5)^2`

    :math:`f_{\\text{DTLZ4}1}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\prod_{i=1}^{m-1} \\cos(0.5x_i^\\alpha\pi)`

    :math:`f_{\\text{DTLZ4}2}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{m-1}^\\alpha\pi ) \\prod_{i=1}^{m-2} \\cos(0.5x_i^\\alpha\pi)`

    :math:`\\ldots`

    :math:`f_{\\text{DTLZ4}m}(\\mathbf{x}) = (1 + g(\\mathbf{x}_m)) \\sin(0.5x_{1}^\\alpha\pi )`

    Where :math:`m` is the number of objectives and :math:`\\mathbf{x}_m` is a
    vector of the remaining attributes :math:`[x_m~\\ldots~x_n]` of the
    variable in :math:`n > m` dimensions.
    """
    xc = variable[:obj - 1]
    xm = variable[obj - 1:]
    g = sum((xi - 0.5) ** 2 for xi in xm)
    f = [(1.0 + g) * reduce(mul, (cos(0.5 * xi ** alpha * pi) for xi in xc), 1.0)]
    f.extend(
        (1.0 + g) * reduce(mul, (cos(0.5 * xi ** alpha * pi) for xi in xc[:m]), 1) * sin(0.5 * xc[m] ** alpha * pi) for
        m in range(obj - 2, -1, -1))
    return f


def fonseca(variable):
    """Fonseca and Fleming's multiobjective function.
    From: C. M. Fonseca and P. J. Fleming, "Multiobjective optimization and
    multiple constraint handling with evolutionary algorithms -- Part II:
    Application example", IEEE Transactions on Systems, Man and Cybernetics,
    1998.

    :math:`f_{\\text{Fonseca}1}(\\mathbf{x}) = 1 - e^{-\\sum_{i=1}^{3}(x_i - \\frac{1}{\\sqrt{3}})^2}`

    :math:`f_{\\text{Fonseca}2}(\\mathbf{x}) = 1 - e^{-\\sum_{i=1}^{3}(x_i + \\frac{1}{\\sqrt{3}})^2}`
    """
    f1 = 1 - exp(-sum((xi - 1 / sqrt(3)) ** 2 for xi in variable[:3]))
    f2 = 1 - exp(-sum((xi + 1 / sqrt(3)) ** 2 for xi in variable[:3]))
    return np.array([f1, f2]).tolist()


def poloni(variable):
    """Poloni's multiobjective function on a two attribute *variable*. From:
    C. Poloni, "Hybrid GA for multi objective aerodynamic shape optimization",
    in Genetic Algorithms in Engineering and Computer Science, 1997.

    :math:`A_1 = 0.5 \\sin (1) - 2 \\cos (1) + \\sin (2) - 1.5 \\cos (2)`

    :math:`A_2 = 1.5 \\sin (1) - \\cos (1) + 2 \\sin (2) - 0.5 \\cos (2)`

    :math:`B_1 = 0.5 \\sin (x_1) - 2 \\cos (x_1) + \\sin (x_2) - 1.5 \\cos (x_2)`

    :math:`B_2 = 1.5 \\sin (x_1) - cos(x_1) + 2 \\sin (x_2) - 0.5 \\cos (x_2)`

    :math:`f_{\\text{Poloni}1}(\\mathbf{x}) = 1 + (A_1 - B_1)^2 + (A_2 - B_2)^2`

    :math:`f_{\\text{Poloni}2}(\\mathbf{x}) = (x_1 + 3)^2 + (x_2 + 1)^2`
    """
    x_1 = variable[0]
    x_2 = variable[1]
    A_1 = 0.5 * sin(1) - 2 * cos(1) + sin(2) - 1.5 * cos(2)
    A_2 = 1.5 * sin(1) - cos(1) + 2 * sin(2) - 0.5 * cos(2)
    B_1 = 0.5 * sin(x_1) - 2 * cos(x_1) + sin(x_2) - 1.5 * cos(x_2)
    B_2 = 1.5 * sin(x_1) - cos(x_1) + 2 * sin(x_2) - 0.5 * cos(x_2)
    return 1 + (A_1 - B_1) ** 2 + (A_2 - B_2) ** 2, (x_1 + 3) ** 2 + (x_2 + 1) ** 2
