import numpy as np
from scipy.stats import norm
from scipy.stats import t

from scipy.stats import chi2
from scipy.stats import chisquare


n = 300

expected = np.array([7.2, 13.2, 99.6, 7.2, 13.2, 99.6, 21.6, 39.6, 298.8])
observed = np.array([6, 20, 94, 10, 13, 97, 20, 33, 307])

chisquare(observed, expected)

chi2_stat = (((observed - expected)**2) / expected).sum()



chi2.cdf(x=chi2_stat, df=4)



np.array([60, 56, 94])

chi2_stat = (30 - 39) ** 2 / 39 + (48 - 39) ** 2 / 39
chi2.cdf(x=chi2_stat, df=1)


democrat = np.array([138, 83, 64])
republican = np.array([64, 67, 84])


mu_a = 0.2
mu_b = 0.25
var_a = mu_a * (1 - mu_a)
var_b = mu_b * (1 - mu_b)

z_975 = 1.96
z_080 = 0.8416


