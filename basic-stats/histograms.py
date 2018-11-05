# Skeleton file for basic exploratory analysis
import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix

import matplotlib as mpl
from matplotlib import pyplot as plt
import hedgeplot as hplt

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


mu = 0
sig = 1
n = 10000
n_bins = 100

norm_x = np.linspace(-5, 5, 10000)
norm_y = scipy.stats.norm.pdf(norm_x)

x = np.random.normal(mu, sig, n)
hist, bins = np.histogram(x, n_bins)
area = np.dot(hist, np.diff(bins))

fig, ax = plt.subplots()
ax.plot(norm_x, norm_y, color='r')
ax.bar(bins[:-1] + np.diff(bins) / 2, hist / area, np.diff(bins), edgecolor='black')
plt.show()

fig, ax = plt.subplots()
ax.plot(norm_x, norm_y, color='r')
ax.hist(x, bins=n_bins, edgecolor='black', density=True)
plt.show()












