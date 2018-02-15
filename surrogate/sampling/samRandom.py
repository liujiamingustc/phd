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

import numpy.random as rand

def samRandom(n=2):
    """samRandom

    :param n: default 2
    :return:

    .. note:: Not sphinx doc!! 20170214
        Encoding: utf-8

        module numpy.random.mtrand

        from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/random/mtrand.so
        by generator 1.138

        no doc

        Links:
            https://docs.scipy.org/doc/numpy/reference/routines.random.html
    """
    return rand.rand(n)


def samBeta(a=0.1, b=0.1, size=None):  # real signature unknown; restored from __doc__
    """beta(a, b, size=None)

    Draw samples from a Beta distribution.

    The Beta distribution is a special case of the Dirichlet distribution,
    and is related to the Gamma distribution.  It has the probability
    distribution function

    .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                     (1 - x)^{\beta - 1},

    where the normalisation, B, is the beta function,

    .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                 (1 - t)^{\beta - 1} dt.

    It is often seen in Bayesian inference and order statistics.

    :param a: Alpha, non-negative
    :type a: float

    :param b: Beta, non-negative
    :type b: float

    :param size: Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                 ``m * n * k`` samples are drawn.  Default is None, in which case a
                 single value is returned.
    :type size: int or tuple of ints, optional

    :returns: out, ndarray
              Array of the given shape, containing values drawn from a
              Beta distribution.
    """
    return rand.beta(a=a, b=b, size=size)


def samBinomial(n=0.1, p=0.5, size=None):  # real signature unknown; restored from __doc__
    """binomial(n, p, size=None)

    Draw samples from a binomial distribution.

    Samples are drawn from a binomial distribution with specified
    parameters, n trials and p probability of success where
    n an integer >= 0 and p is in the interval [0,1]. (n may be
    input as a float, but it is truncated to an integer in use)

    Parameters
    ----------
    n : float (but truncated to an integer)
            parameter, >= 0.
    p : float
            parameter, >= 0 and <=1.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
              where the values are all integers in  [0, n].

    See Also
    --------
    scipy.stats.distributions.binom : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The probability density for the binomial distribution is

    .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},

    where :math:`n` is the number of trials, :math:`p` is the probability
    of success, and :math:`N` is the number of successes.

    When estimating the standard error of a proportion in a population by
    using a random sample, the normal distribution works well unless the
    product p*n <=5, where p = population proportion estimate, and n =
    number of samples, in which case the binomial distribution is used
    instead. For example, a sample of 15 people shows 4 who are left
    handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
    so the binomial distribution should be used in this case.

    References
    ----------
    .. [1] Dalgaard, Peter, "Introductory Statistics with R",
           Springer-Verlag, 2002.
    .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
           Fifth Edition, 2002.
    .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
           and Quigley, 1972.
    .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
           Wolfram Web Resource.
           http://mathworld.wolfram.com/BinomialDistribution.html
    .. [5] Wikipedia, "Binomial-distribution",
           http://en.wikipedia.org/wiki/Binomial_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> n, p = 10, .5  # number of trials, probability of each trial
    >>> s = np.random.binomial(n, p, 1000)
    # result of flipping a coin 10 times, tested 1000 times.

    A real world example. A company drills 9 wild-cat oil exploration
    wells, each with an estimated probability of success of 0.1. All nine
    wells fail. What is the probability of that happening?

    Let's do 20,000 trials of the model, and count the number that
    generate zero positive results.

    >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
    # answer = 0.38885, or 38%.
    """
    return rand.binomial(n=n, p=p, size=size)


def samChiSquare(df=2, size=None):  # real signature unknown; restored from __doc__
    """chisquare(df, size=None)

    Draw samples from a chi-square distribution.

    When `df` independent random variables, each with standard normal
    distributions (mean 0, variance 1), are squared and summed, the
    resulting distribution is chi-square (see Notes).  This distribution
    is often used in hypothesis testing.

    Parameters
    ----------
    df : int
         Number of degrees of freedom.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    output : ndarray
        Samples drawn from the distribution, packed in a `size`-shaped
        array.

    Raises
    ------
    ValueError
        When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
        is given.

    Notes
    -----
    The variable obtained by summing the squares of `df` independent,
    standard normally distributed random variables:

    .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i

    is chi-square distributed, denoted

    .. math:: Q \sim \chi^2_k.

    The probability density function of the chi-squared distribution is

    .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
                     x^{k/2 - 1} e^{-x/2},

    where :math:`\Gamma` is the gamma function,

    .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.

    References
    ----------
    .. [1] NIST "Engineering Statistics Handbook"
           http://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm

    Examples
    --------
    >>> np.random.chisquare(2,4)
    array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272])
    """
    return rand.chisquare(df=df, size=size)


def samExponential(scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """exponential(scale=1.0, size=None)

    Draw samples from an exponential distribution.

    Its probability density function is

    .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),

    for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
    which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
    The rate parameter is an alternative, widely used parameterization
    of the exponential distribution [3]_.

    The exponential distribution is a continuous analogue of the
    geometric distribution.  It describes many common situations, such as
    the size of raindrops measured over many rainstorms [1]_, or the time
    between page requests to Wikipedia [2]_.

    Parameters
    ----------
    scale : float
        The scale parameter, :math:`\beta = 1/\lambda`.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    References
    ----------
    .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
           Random Signal Principles", 4th ed, 2001, p. 57.
    .. [2] "Poisson Process", Wikipedia,
           http://en.wikipedia.org/wiki/Poisson_process
    .. [3] "Exponential Distribution, Wikipedia,
           http://en.wikipedia.org/wiki/Exponential_distribution
    """
    return rand.exponential(scale=scale, size=size)


def samF(dfnum=1, dfden=48, size=None):  # real signature unknown; restored from __doc__
    """f(dfnum, dfden, size=None)

    Draw samples from an F distribution.

    Samples are drawn from an F distribution with specified parameters,
    `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
    freedom in denominator), where both parameters should be greater than
    zero.

    The random variate of the F distribution (also known as the
    Fisher distribution) is a continuous probability distribution
    that arises in ANOVA tests, and is the ratio of two chi-square
    variates.

    Parameters
    ----------
    dfnum : float
        Degrees of freedom in numerator. Should be greater than zero.
    dfden : float
        Degrees of freedom in denominator. Should be greater than zero.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
        Samples from the Fisher distribution.

    See Also
    --------
    scipy.stats.distributions.f : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The F statistic is used to compare in-group variances to between-group
    variances. Calculating the distribution depends on the sampling, and
    so it is a function of the respective degrees of freedom in the
    problem.  The variable `dfnum` is the number of samples minus one, the
    between-groups degrees of freedom, while `dfden` is the within-groups
    degrees of freedom, the sum of the number of samples in each group
    minus the number of groups.

    References
    ----------
    .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
           Fifth Edition, 2002.
    .. [2] Wikipedia, "F-distribution",
           http://en.wikipedia.org/wiki/F-distribution

    Examples
    --------
    An example from Glantz[1], pp 47-40:

    Two groups, children of diabetics (25 people) and children from people
    without diabetes (25 controls). Fasting blood glucose was measured,
    case group had a mean value of 86.1, controls had a mean value of
    82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
    data consistent with the null hypothesis that the parents diabetic
    status does not affect their children's blood glucose levels?
    Calculating the F statistic from the data gives a value of 36.01.

    Draw samples from the distribution:

    >>> dfnum = 1. # between group degrees of freedom
    >>> dfden = 48. # within groups degrees of freedom
    >>> s = np.random.f(dfnum, dfden, 1000)

    The lower bound for the top 1% of the samples is :

    >>> sort(s)[-10]
    7.61988120985

    So there is about a 1% chance that the F statistic will exceed 7.62,
    the measured value is 36, so the null hypothesis is rejected at the 1%
    level.
    """
    return rand.f(dfnum=dfnum, dfden=dfden, size=size)


def samGamma(shape=2.0, scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """gamma(shape, scale=1.0, size=None)

    Draw samples from a Gamma distribution.

    Samples are drawn from a Gamma distribution with specified parameters,
    `shape` (sometimes designated "k") and `scale` (sometimes designated
    "theta"), where both parameters are > 0.

    Parameters
    ----------
    shape : scalar > 0
        The shape of the gamma distribution.
    scale : scalar > 0, optional
        The scale of the gamma distribution.  Default is equal to 1.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    out : ndarray, float
        Returns one sample unless `size` parameter is specified.

    See Also
    --------
    scipy.stats.distributions.gamma : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The probability density for the Gamma distribution is

    .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},

    where :math:`k` is the shape and :math:`\theta` the scale,
    and :math:`\Gamma` is the Gamma function.

    The Gamma distribution is often used to model the times to failure of
    electronic components, and arises naturally in processes for which the
    waiting times between Poisson distributed events are relevant.

    References
    ----------
    .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
           Wolfram Web Resource.
           http://mathworld.wolfram.com/GammaDistribution.html
    .. [2] Wikipedia, "Gamma-distribution",
           http://en.wikipedia.org/wiki/Gamma-distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> shape, scale = 2., 2. # mean and dispersion
    >>> s = np.random.gamma(shape, scale, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> import scipy.special as sps
    >>> count, bins, ignored = plt.hist(s, 50, normed=True)
    >>> y = bins**(shape-1)*(np.exp(-bins/scale) /
    ...                      (sps.gamma(shape)*scale**shape))
    >>> plt.plot(bins, y, linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.gamma(shape=shape, scale=scale, size=size)


def samGumbel(loc=0.0, scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """gumbel(loc=0.0, scale=1.0, size=None)

    Draw samples from a Gumbel distribution.

    Draw samples from a Gumbel distribution with specified location and
    scale.  For more information on the Gumbel distribution, see
    Notes and References below.

    Parameters
    ----------
    loc : float
        The location of the mode of the distribution.
    scale : float
        The scale parameter of the distribution.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar

    See Also
    --------
    scipy.stats.gumbel_l
    scipy.stats.gumbel_r
    scipy.stats.genextreme
    weibull

    Notes
    -----
    The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
    Value Type I) distribution is one of a class of Generalized Extreme
    Value (GEV) distributions used in modeling extreme value problems.
    The Gumbel is a special case of the Extreme Value Type I distribution
    for maximums from distributions with "exponential-like" tails.

    The probability density for the Gumbel distribution is

    .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
              \beta}},

    where :math:`\mu` is the mode, a location parameter, and
    :math:`\beta` is the scale parameter.

    The Gumbel (named for German mathematician Emil Julius Gumbel) was used
    very early in the hydrology literature, for modeling the occurrence of
    flood events. It is also used for modeling maximum wind speed and
    rainfall rates.  It is a "fat-tailed" distribution - the probability of
    an event in the tail of the distribution is larger than if one used a
    Gaussian, hence the surprisingly frequent occurrence of 100-year
    floods. Floods were initially modeled as a Gaussian process, which
    underestimated the frequency of extreme events.

    It is one of a class of extreme value distributions, the Generalized
    Extreme Value (GEV) distributions, which also includes the Weibull and
    Frechet.

    The function has a mean of :math:`\mu + 0.57721\beta` and a variance
    of :math:`\frac{\pi^2}{6}\beta^2`.

    References
    ----------
    .. [1] Gumbel, E. J., "Statistics of Extremes,"
           New York: Columbia University Press, 1958.
    .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
           Values from Insurance, Finance, Hydrology and Other Fields,"
           Basel: Birkhauser Verlag, 2001.

    Examples
    --------
    Draw samples from the distribution:

    >>> mu, beta = 0, 0.1 # location and scale
    >>> s = np.random.gumbel(mu, beta, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 30, normed=True)
    >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
    ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
    ...          linewidth=2, color='r')
    >>> plt.show()

    Show how an extreme value distribution can arise from a Gaussian process
    and compare to a Gaussian:

    >>> means = []
    >>> maxima = []
    >>> for i in range(0,1000) :
    ...    a = np.random.normal(mu, beta, 1000)
    ...    means.append(a.mean())
    ...    maxima.append(a.max())
    >>> count, bins, ignored = plt.hist(maxima, 30, normed=True)
    >>> beta = np.std(maxima)*np.pi/np.sqrt(6)
    >>> mu = np.mean(maxima) - 0.57721*beta
    >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
    ...          * np.exp(-np.exp(-(bins - mu)/beta)),
    ...          linewidth=2, color='r')
    >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
    ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
    ...          linewidth=2, color='g')
    >>> plt.show()
    """
    return rand.gumbel(loc=loc, scale=scale, size=size)


def samLaplace(loc=0.0, scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """laplace(loc=0.0, scale=1.0, size=None)

    Draw samples from the Laplace or double exponential distribution with
    specified location (or mean) and scale (decay).

    The Laplace distribution is similar to the Gaussian/normal distribution,
    but is sharper at the peak and has fatter tails. It represents the
    difference between two independent, identically distributed exponential
    random variables.

    Parameters
    ----------
    loc : float, optional
        The position, :math:`\mu`, of the distribution peak.
    scale : float, optional
        :math:`\lambda`, the exponential decay.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or float

    Notes
    -----
    It has the probability density function

    .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
                                   \exp\left(-\frac{|x - \mu|}{\lambda}\right).

    The first law of Laplace, from 1774, states that the frequency
    of an error can be expressed as an exponential function of the
    absolute magnitude of the error, which leads to the Laplace
    distribution. For many problems in economics and health
    sciences, this distribution seems to model the data better
    than the standard Gaussian distribution.

    References
    ----------
    .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
           Mathematical Functions with Formulas, Graphs, and Mathematical
           Tables, 9th printing," New York: Dover, 1972.
    .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
           Generalizations, " Birkhauser, 2001.
    .. [3] Weisstein, Eric W. "Laplace Distribution."
           From MathWorld--A Wolfram Web Resource.
           http://mathworld.wolfram.com/LaplaceDistribution.html
    .. [4] Wikipedia, "Laplace Distribution",
           http://en.wikipedia.org/wiki/Laplace_distribution

    Examples
    --------
    Draw samples from the distribution

    >>> loc, scale = 0., 1.
    >>> s = np.random.laplace(loc, scale, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 30, normed=True)
    >>> x = np.arange(-8., 8., .01)
    >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
    >>> plt.plot(x, pdf)

    Plot Gaussian for comparison:

    >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
    ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
    >>> plt.plot(x,g)
    """
    return rand.laplace(loc=loc, scale=scale, size=size)


def samLogistic(loc=0.0, scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """logistic(loc=0.0, scale=1.0, size=None)

    Draw samples from a logistic distribution.

    Samples are drawn from a logistic distribution with specified
    parameters, loc (location or mean, also median), and scale (>0).

    Parameters
    ----------
    loc : float

    scale : float > 0.

    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
              where the values are all integers in  [0, n].

    See Also
    --------
    scipy.stats.distributions.logistic : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The probability density for the Logistic distribution is

    .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},

    where :math:`\mu` = location and :math:`s` = scale.

    The Logistic distribution is used in Extreme Value problems where it
    can act as a mixture of Gumbel distributions, in Epidemiology, and by
    the World Chess Federation (FIDE) where it is used in the Elo ranking
    system, assuming the performance of each player is a logistically
    distributed random variable.

    References
    ----------
    .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
           Extreme Values, from Insurance, Finance, Hydrology and Other
           Fields," Birkhauser Verlag, Basel, pp 132-133.
    .. [2] Weisstein, Eric W. "Logistic Distribution." From
           MathWorld--A Wolfram Web Resource.
           http://mathworld.wolfram.com/LogisticDistribution.html
    .. [3] Wikipedia, "Logistic-distribution",
           http://en.wikipedia.org/wiki/Logistic_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> loc, scale = 10, 1
    >>> s = np.random.logistic(loc, scale, 10000)
    >>> count, bins, ignored = plt.hist(s, bins=50)

    #   plot against distribution

    >>> def logist(x, loc, scale):
    ...     return exp((loc-x)/scale)/(scale*(1+exp((loc-x)/scale))**2)
    >>> plt.plot(bins, logist(bins, loc, scale)*count.max()/\
    ... logist(bins, loc, scale).max())
    >>> plt.show()
    """
    return rand.logistic(loc=loc, scale=scale, size=size)


def samLognormal(mean=0.0, sigma=1.0, size=None):  # real signature unknown; restored from __doc__
    """lognormal(mean=0.0, sigma=1.0, size=None)

    Draw samples from a log-normal distribution.

    Draw samples from a log-normal distribution with specified mean,
    standard deviation, and array shape.  Note that the mean and standard
    deviation are not the values for the distribution itself, but of the
    underlying normal distribution it is derived from.

    Parameters
    ----------
    mean : float
        Mean value of the underlying normal distribution
    sigma : float, > 0.
        Standard deviation of the underlying normal distribution
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or float
        The desired samples. An array of the same shape as `size` if given,
        if `size` is None a float is returned.

    See Also
    --------
    scipy.stats.lognorm : probability density function, distribution,
        cumulative density function, etc.

    Notes
    -----
    A variable `x` has a log-normal distribution if `log(x)` is normally
    distributed.  The probability density function for the log-normal
    distribution is:

    .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
                     e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}

    where :math:`\mu` is the mean and :math:`\sigma` is the standard
    deviation of the normally distributed logarithm of the variable.
    A log-normal distribution results if a random variable is the *product*
    of a large number of independent, identically-distributed variables in
    the same way that a normal distribution results if the variable is the
    *sum* of a large number of independent, identically-distributed
    variables.

    References
    ----------
    .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
           Distributions across the Sciences: Keys and Clues,"
           BioScience, Vol. 51, No. 5, May, 2001.
           http://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
    .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
           Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.

    Examples
    --------
    Draw samples from the distribution:

    >>> mu, sigma = 3., 1. # mean and standard deviation
    >>> s = np.random.lognormal(mu, sigma, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')

    >>> x = np.linspace(min(bins), max(bins), 10000)
    >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
    ...        / (x * sigma * np.sqrt(2 * np.pi)))

    >>> plt.plot(x, pdf, linewidth=2, color='r')
    >>> plt.axis('tight')
    >>> plt.show()

    Demonstrate that taking the products of random samples from a uniform
    distribution can be fit well by a log-normal probability density
    function.

    >>> # Generate a thousand samples: each is the product of 100 random
    >>> # values, drawn from a normal distribution.
    >>> b = []
    >>> for i in range(1000):
    ...    a = 10. + np.random.random(100)
    ...    b.append(np.product(a))

    >>> b = np.array(b) / np.min(b) # scale values to be positive
    >>> count, bins, ignored = plt.hist(b, 100, normed=True, align='mid')
    >>> sigma = np.std(np.log(b))
    >>> mu = np.mean(np.log(b))

    >>> x = np.linspace(min(bins), max(bins), 10000)
    >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
    ...        / (x * sigma * np.sqrt(2 * np.pi)))

    >>> plt.plot(x, pdf, color='r', linewidth=2)
    >>> plt.show()
    """
    return rand.lognormal(mean=mean, sigma=sigma, size=size)


def samNormal(loc=0.0, scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """normal(loc=0.0, scale=1.0, size=None)

    Draw random samples from a normal (Gaussian) distribution.

    The probability density function of the normal distribution, first
    derived by De Moivre and 200 years later by both Gauss and Laplace
    independently [2]_, is often called the bell curve because of
    its characteristic shape (see the example below).

    The normal distributions occurs often in nature.  For example, it
    describes the commonly occurring distribution of samples influenced
    by a large number of tiny, random disturbances, each with its own
    unique distribution [2]_.

    Parameters
    ----------
    loc : float
        Mean ("centre") of the distribution.
    scale : float
        Standard deviation (spread or "width") of the distribution.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    See Also
    --------
    scipy.stats.distributions.norm : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The probability density for the Gaussian distribution is

    .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
                     e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },

    where :math:`\mu` is the mean and :math:`\sigma` the standard
    deviation. The square of the standard deviation, :math:`\sigma^2`,
    is called the variance.

    The function has its peak at the mean, and its "spread" increases with
    the standard deviation (the function reaches 0.607 times its maximum at
    :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
    `numpy.random.normal` is more likely to return samples lying close to
    the mean, rather than those far away.

    References
    ----------
    .. [1] Wikipedia, "Normal distribution",
           http://en.wikipedia.org/wiki/Normal_distribution
    .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
           Random Variables and Random Signal Principles", 4th ed., 2001,
           pp. 51, 51, 125.

    Examples
    --------
    Draw samples from the distribution:

    >>> mu, sigma = 0, 0.1 # mean and standard deviation
    >>> s = np.random.normal(mu, sigma, 1000)

    Verify the mean and the variance:

    >>> abs(mu - np.mean(s)) < 0.01
    True

    >>> abs(sigma - np.std(s, ddof=1)) < 0.01
    True

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 30, normed=True)
    >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
    ...          linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.normal(loc=loc, scale=scale, size=size)


def samPareto(a=3.0, size=None):  # real signature unknown; restored from __doc__
    """pareto(a, size=None)

    Draw samples from a Pareto II or Lomax distribution with
    specified shape.

    The Lomax or Pareto II distribution is a shifted Pareto
    distribution. The classical Pareto distribution can be
    obtained from the Lomax distribution by adding 1 and
    multiplying by the scale parameter ``m`` (see Notes).  The
    smallest value of the Lomax distribution is zero while for the
    classical Pareto distribution it is ``mu``, where the standard
    Pareto distribution has location ``mu = 1``.  Lomax can also
    be considered as a simplified version of the Generalized
    Pareto distribution (available in SciPy), with the scale set
    to one and the location set to zero.

    The Pareto distribution must be greater than zero, and is
    unbounded above.  It is also known as the "80-20 rule".  In
    this distribution, 80 percent of the weights are in the lowest
    20 percent of the range, while the other 20 percent fill the
    remaining 80 percent of the range.

    Parameters
    ----------
    shape : float, > 0.
        Shape of the distribution.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    See Also
    --------
    scipy.stats.distributions.lomax.pdf : probability density function,
        distribution or cumulative density function, etc.
    scipy.stats.distributions.genpareto.pdf : probability density function,
        distribution or cumulative density function, etc.

    Notes
    -----
    The probability density for the Pareto distribution is

    .. math:: p(x) = \frac{am^a}{x^{a+1}}

    where :math:`a` is the shape and :math:`m` the scale.

    The Pareto distribution, named after the Italian economist
    Vilfredo Pareto, is a power law probability distribution
    useful in many real world problems.  Outside the field of
    economics it is generally referred to as the Bradford
    distribution. Pareto developed the distribution to describe
    the distribution of wealth in an economy.  It has also found
    use in insurance, web page access statistics, oil field sizes,
    and many other problems, including the download frequency for
    projects in Sourceforge [1]_.  It is one of the so-called
    "fat-tailed" distributions.


    References
    ----------
    .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
           Sourceforge projects.
    .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
    .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
           Values, Birkhauser Verlag, Basel, pp 23-30.
    .. [4] Wikipedia, "Pareto distribution",
           http://en.wikipedia.org/wiki/Pareto_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> a, m = 3., 2.  # shape and mode
    >>> s = (np.random.pareto(a, 1000) + 1) * m

    Display the histogram of the samples, along with the probability
    density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, _ = plt.hist(s, 100, normed=True)
    >>> fit = a*m**a / bins**(a+1)
    >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.pareto(a=a, size=size)


def samPoisson(lam=1.0, size=None):  # real signature unknown; restored from __doc__
    """poisson(lam=1.0, size=None)

    Draw samples from a Poisson distribution.

    The Poisson distribution is the limit of the binomial distribution
    for large N.

    Parameters
    ----------
    lam : float or sequence of float
        Expectation of interval, should be >= 0. A sequence of expectation
        intervals must be broadcastable over the requested size.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
        The drawn samples, of shape *size*, if it was provided.

    Notes
    -----
    The Poisson distribution

    .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}

    For events with an expected separation :math:`\lambda` the Poisson
    distribution :math:`f(k; \lambda)` describes the probability of
    :math:`k` events occurring within the observed
    interval :math:`\lambda`.

    Because the output is limited to the range of the C long type, a
    ValueError is raised when `lam` is within 10 sigma of the maximum
    representable value.

    References
    ----------
    .. [1] Weisstein, Eric W. "Poisson Distribution."
           From MathWorld--A Wolfram Web Resource.
           http://mathworld.wolfram.com/PoissonDistribution.html
    .. [2] Wikipedia, "Poisson distribution",
           http://en.wikipedia.org/wiki/Poisson_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> import numpy as np
    >>> s = np.random.poisson(5, 10000)

    Display histogram of the sample:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 14, normed=True)
    >>> plt.show()

    Draw each 100 values for lambda 100 and 500:

    >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))
    """
    return rand.poisson(lam=lam, size=size)


def samPower(a=5.0, size=None):  # real signature unknown; restored from __doc__
    """power(a, size=None)

    Draws samples in [0, 1] from a power distribution with positive
    exponent a - 1.

    Also known as the power function distribution.

    Parameters
    ----------
    a : float
        parameter, > 0
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
        The returned samples lie in [0, 1].

    Raises
    ------
    ValueError
        If a < 1.

    Notes
    -----
    The probability density function is

    .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.

    The power function distribution is just the inverse of the Pareto
    distribution. It may also be seen as a special case of the Beta
    distribution.

    It is used, for example, in modeling the over-reporting of insurance
    claims.

    References
    ----------
    .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
           in economics and actuarial sciences", Wiley, 2003.
    .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
           Dataplot Reference Manual, Volume 2: Let Subcommands and Library
           Functions", National Institute of Standards and Technology
           Handbook Series, June 2003.
           http://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf

    Examples
    --------
    Draw samples from the distribution:

    >>> a = 5. # shape
    >>> samples = 1000
    >>> s = np.random.power(a, samples)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, bins=30)
    >>> x = np.linspace(0, 1, 100)
    >>> y = a*x**(a-1.)
    >>> normed_y = samples*np.diff(bins)[0]*y
    >>> plt.plot(x, normed_y)
    >>> plt.show()

    Compare the power function distribution to the inverse of the Pareto.

    >>> from scipy import stats
    >>> rvs = np.random.power(5, 1000000)
    >>> rvsp = np.random.pareto(5, 1000000)
    >>> xx = np.linspace(0,1,100)
    >>> powpdf = stats.powerlaw.pdf(xx,5)

    >>> plt.figure()
    >>> plt.hist(rvs, bins=50, normed=True)
    >>> plt.plot(xx,powpdf,'r-')
    >>> plt.title('np.random.power(5)')

    >>> plt.figure()
    >>> plt.hist(1./(1.+rvsp), bins=50, normed=True)
    >>> plt.plot(xx,powpdf,'r-')
    >>> plt.title('inverse of 1 + np.random.pareto(5)')

    >>> plt.figure()
    >>> plt.hist(1./(1.+rvsp), bins=50, normed=True)
    >>> plt.plot(xx,powpdf,'r-')
    >>> plt.title('inverse of stats.pareto(5)')
    """
    return rand.power(a=a, size=size)


def samRayleigh(scale=1.0, size=None):  # real signature unknown; restored from __doc__
    """rayleigh(scale=1.0, size=None)

    Draw samples from a Rayleigh distribution.

    The :math:`\chi` and Weibull distributions are generalizations of the
    Rayleigh.

    Parameters
    ----------
    scale : scalar
        Scale, also equals the mode. Should be >= 0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Notes
    -----
    The probability density function for the Rayleigh distribution is

    .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}

    The Rayleigh distribution would arise, for example, if the East
    and North components of the wind velocity had identical zero-mean
    Gaussian distributions.  Then the wind speed would have a Rayleigh
    distribution.

    References
    ----------
    .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
           http://www.brighton-webs.co.uk/distributions/rayleigh.asp
    .. [2] Wikipedia, "Rayleigh distribution"
           http://en.wikipedia.org/wiki/Rayleigh_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram

    >>> values = hist(np.random.rayleigh(3, 100000), bins=200, normed=True)

    Wave heights tend to follow a Rayleigh distribution. If the mean wave
    height is 1 meter, what fraction of waves are likely to be larger than 3
    meters?

    >>> meanvalue = 1
    >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
    >>> s = np.random.rayleigh(modevalue, 1000000)

    The percentage of waves larger than 3 meters is:

    >>> 100.*sum(s>3)/1000000.
    0.087300000000000003
    """
    return rand.rayleigh(scale=scale, size=size)


def samTriangular(left=-3, mode=0, right=8, size=None):  # real signature unknown; restored from __doc__
    """triangular(left, mode, right, size=None)

    Draw samples from the triangular distribution.

    The triangular distribution is a continuous probability
    distribution with lower limit left, peak at mode, and upper
    limit right. Unlike the other distributions, these parameters
    directly define the shape of the pdf.

    Parameters
    ----------
    left : scalar
        Lower limit.
    mode : scalar
        The value where the peak of the distribution occurs.
        The value should fulfill the condition ``left <= mode <= right``.
    right : scalar
        Upper limit, should be larger than `left`.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
        The returned samples all lie in the interval [left, right].

    Notes
    -----
    The probability density function for the triangular distribution is

    .. math:: P(x;l, m, r) = \begin{cases}
              \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
              \frac{2(m-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
              0& \text{otherwise}.
              \end{cases}

    The triangular distribution is often used in ill-defined
    problems where the underlying distribution is not known, but
    some knowledge of the limits and mode exists. Often it is used
    in simulations.

    References
    ----------
    .. [1] Wikipedia, "Triangular distribution"
           http://en.wikipedia.org/wiki/Triangular_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram:

    >>> import matplotlib.pyplot as plt
    >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
    ...              normed=True)
    >>> plt.show()
    """
    return rand.triangular(left=left, mode=mode, right=right, size=size)


def samUniform(low=0.0, high=1.0, size=None):  # real signature unknown; restored from __doc__
    """uniform(low=0.0, high=1.0, size=None)

    Draw samples from a uniform distribution.

    Samples are uniformly distributed over the half-open interval
    ``[low, high)`` (includes low, but excludes high).  In other words,
    any value within the given interval is equally likely to be drawn
    by `uniform`.

    Parameters
    ----------
    low : float, optional
        Lower boundary of the output interval.  All values generated will be
        greater than or equal to low.  The default value is 0.
    high : float
        Upper boundary of the output interval.  All values generated will be
        less than high.  The default value is 1.0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    out : ndarray
        Drawn samples, with shape `size`.

    See Also
    --------
    randint : Discrete uniform distribution, yielding integers.
    random_integers : Discrete uniform distribution over the closed
                      interval ``[low, high]``.
    random_sample : Floats uniformly distributed over ``[0, 1)``.
    random : Alias for `random_sample`.
    rand : Convenience function that accepts dimensions as input, e.g.,
           ``rand(2,2)`` would generate a 2-by-2 array of floats,
           uniformly distributed over ``[0, 1)``.

    Notes
    -----
    The probability density function of the uniform distribution is

    .. math:: p(x) = \frac{1}{b - a}

    anywhere within the interval ``[a, b)``, and zero elsewhere.

    Examples
    --------
    Draw samples from the distribution:

    >>> s = np.random.uniform(-1,0,1000)

    All values are within the given interval:

    >>> np.all(s >= -1)
    True
    >>> np.all(s < 0)
    True

    Display the histogram of the samples, along with the
    probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 15, normed=True)
    >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.uniform(low=low, high=high, size=size)


def samVonmises(mu=0.0, kappa=4.0, size=None):  # real signature unknown; restored from __doc__
    """vonmises(mu, kappa, size=None)

    Draw samples from a von Mises distribution.

    Samples are drawn from a von Mises distribution with specified mode
    (mu) and dispersion (kappa), on the interval [-pi, pi].

    The von Mises distribution (also known as the circular normal
    distribution) is a continuous probability distribution on the unit
    circle.  It may be thought of as the circular analogue of the normal
    distribution.

    Parameters
    ----------
    mu : float
        Mode ("center") of the distribution.
    kappa : float
        Dispersion of the distribution, has to be >=0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : scalar or ndarray
        The returned samples, which are in the interval [-pi, pi].

    See Also
    --------
    scipy.stats.distributions.vonmises : probability density function,
        distribution, or cumulative density function, etc.

    Notes
    -----
    The probability density for the von Mises distribution is

    .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},

    where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
    and :math:`I_0(\kappa)` is the modified Bessel function of order 0.

    The von Mises is named for Richard Edler von Mises, who was born in
    Austria-Hungary, in what is now the Ukraine.  He fled to the United
    States in 1939 and became a professor at Harvard.  He worked in
    probability theory, aerodynamics, fluid mechanics, and philosophy of
    science.

    References
    ----------
    .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
           Mathematical Functions with Formulas, Graphs, and Mathematical
           Tables, 9th printing," New York: Dover, 1972.
    .. [2] von Mises, R., "Mathematical Theory of Probability
           and Statistics", New York: Academic Press, 1964.

    Examples
    --------
    Draw samples from the distribution:

    >>> mu, kappa = 0.0, 4.0 # mean and dispersion
    >>> s = np.random.vonmises(mu, kappa, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> from scipy.special import i0
    >>> plt.hist(s, 50, normed=True)
    >>> x = np.linspace(-np.pi, np.pi, num=51)
    >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))
    >>> plt.plot(x, y, linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.vonmises(mu=mu, kappa=kappa, size=size)


def samWald(mean=3, scale=2, size=None):  # real signature unknown; restored from __doc__
    """wald(mean, scale, size=None)

    Draw samples from a Wald, or inverse Gaussian, distribution.

    As the scale approaches infinity, the distribution becomes more like a
    Gaussian. Some references claim that the Wald is an inverse Gaussian
    with mean equal to 1, but this is by no means universal.

    The inverse Gaussian distribution was first studied in relationship to
    Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
    because there is an inverse relationship between the time to cover a
    unit distance and distance covered in unit time.

    Parameters
    ----------
    mean : scalar
        Distribution mean, should be > 0.
    scale : scalar
        Scale parameter, should be >= 0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray or scalar
        Drawn sample, all greater than zero.

    Notes
    -----
    The probability density function for the Wald distribution is

    .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
                                \frac{-scale(x-mean)^2}{2\cdotp mean^2x}

    As noted above the inverse Gaussian distribution first arise
    from attempts to model Brownian motion. It is also a
    competitor to the Weibull for use in reliability modeling and
    modeling stock returns and interest rate processes.

    References
    ----------
    .. [1] Brighton Webs Ltd., Wald Distribution,
           http://www.brighton-webs.co.uk/distributions/wald.asp
    .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
           Distribution: Theory : Methodology, and Applications", CRC Press,
           1988.
    .. [3] Wikipedia, "Wald distribution"
           http://en.wikipedia.org/wiki/Wald_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram:

    >>> import matplotlib.pyplot as plt
    >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, normed=True)
    >>> plt.show()
    """
    return rand.wald(mean=mean, scale=scale, size=size)


def samWeibull(a=5.0, size=None):  # real signature unknown; restored from __doc__
    """weibull(a, size=None)

    Draw samples from a Weibull distribution.

    Draw samples from a 1-parameter Weibull distribution with the given
    shape parameter `a`.

    .. math:: X = (-ln(U))^{1/a}

    Here, U is drawn from the uniform distribution over (0,1].

    The more common 2-parameter Weibull, including a scale parameter
    :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.

    Parameters
    ----------
    a : float
        Shape of the distribution.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : ndarray

    See Also
    --------
    scipy.stats.distributions.weibull_max
    scipy.stats.distributions.weibull_min
    scipy.stats.distributions.genextreme
    gumbel

    Notes
    -----
    The Weibull (or Type III asymptotic extreme value distribution
    for smallest values, SEV Type III, or Rosin-Rammler
    distribution) is one of a class of Generalized Extreme Value
    (GEV) distributions used in modeling extreme value problems.
    This class includes the Gumbel and Frechet distributions.

    The probability density for the Weibull distribution is

    .. math:: p(x) = \frac{a}
                     {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},

    where :math:`a` is the shape and :math:`\lambda` the scale.

    The function has its peak (the mode) at
    :math:`\lambda(\frac{a-1}{a})^{1/a}`.

    When ``a = 1``, the Weibull distribution reduces to the exponential
    distribution.

    References
    ----------
    .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
           1939 "A Statistical Theory Of The Strength Of Materials",
           Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
           Generalstabens Litografiska Anstalts Forlag, Stockholm.
    .. [2] Waloddi Weibull, "A Statistical Distribution Function of
           Wide Applicability", Journal Of Applied Mechanics ASME Paper
           1951.
    .. [3] Wikipedia, "Weibull distribution",
           http://en.wikipedia.org/wiki/Weibull_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> a = 5. # shape
    >>> s = np.random.weibull(a, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> x = np.arange(1,100.)/50.
    >>> def weib(x,n,a):
    ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

    >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
    >>> x = np.arange(1,100.)/50.
    >>> scale = count.max()/weib(x, 1., 5.).max()
    >>> plt.plot(x, weib(x, 1., 5.)*scale)
    >>> plt.show()
    """
    return rand.weibull(a=a, size=size)


def samZipf(a=2.0, size=None):  # real signature unknown; restored from __doc__
    """zipf(a, size=None)

    Draw samples from a Zipf distribution.

    Samples are drawn from a Zipf distribution with specified parameter
    `a` > 1.

    The Zipf distribution (also known as the zeta distribution) is a
    continuous probability distribution that satisfies Zipf's law: the
    frequency of an item is inversely proportional to its rank in a
    frequency table.

    Parameters
    ----------
    a : float > 1
        Distribution parameter.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    samples : scalar or ndarray
        The returned samples are greater than or equal to one.

    See Also
    --------
    scipy.stats.distributions.zipf : probability density function,
        distribution, or cumulative density function, etc.

    Notes
    -----
    The probability density for the Zipf distribution is

    .. math:: p(x) = \frac{x^{-a}}{\zeta(a)},

    where :math:`\zeta` is the Riemann Zeta function.

    It is named for the American linguist George Kingsley Zipf, who noted
    that the frequency of any word in a sample of a language is inversely
    proportional to its rank in the frequency table.

    References
    ----------
    .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
           Frequency in Language," Cambridge, MA: Harvard Univ. Press,
           1932.

    Examples
    --------
    Draw samples from the distribution:

    >>> a = 2. # parameter
    >>> s = np.random.zipf(a, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> import scipy.special as sps
    Truncate s values at 50 so plot is interesting
    >>> count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
    >>> x = np.arange(1., 50.)
    >>> y = x**(-a)/sps.zetac(a)
    >>> plt.plot(x, y/max(y), linewidth=2, color='r')
    >>> plt.show()
    """
    return rand.zipf(a=a, size=size)
