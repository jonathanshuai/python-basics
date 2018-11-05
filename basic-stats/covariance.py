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

n = 200
domain = np.pi * 3
mu = 0
sig = 0.1
y_transform = lambda x: np.sin(x) 

x = np.random.rand(n) * domain # Uniform distirbution
y = y_transform(x)
y += np.random.normal(mu, sig, n) # Some gaussian noise

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()


covariance = np.dot(x - np.mean(x), y - np.mean(y)) / (n - 1)  
correlation = np.corrcoef(x, y)
print("Covariance: {}".format(covariance))
print("--Correlation--\n {}".format(correlation))









