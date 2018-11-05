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
import seaborn as sns


import time
from datetime import datetime
import dateutil

# import pendulum

# import statsmodels.api as sm
# from statsmodels.stats.outliers_influence import variance_inflation_factor

data_file = './data/SalaryData.csv'
df = pd.read_csv(data_file) 

sns.lmplot(x='YearsExperience', y='Salary', data=df)
plt.show()


from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(df[['YearsExperience']], df['Salary'])

x = np.linspace(0, 12, 100)
y = clf.predict(x.reshape(-1, 1))

plt.plot(x, y)
plt.scatter(df['YearsExperience'], df['Salary'])
plt.show()

def confidence_interval(x_i, x_mean, ss_x, t_value, n, mse):
  return t_value * np.sqrt(mse * ((1/n) + ((x_i - x_mean)**2) / ss_x))

p = 0.05

x_mean = df['YearsExperience'].mean()
n = len(df['YearsExperience'])
ss_x = df['YearsExperience'].var() * (n - 1)
t_value = scipy.stats.t.ppf(1 - p / 2, n - 2)

mse = mean_squared_error(clf.predict(df[['YearsExperience']]), df['Salary'])


ci = [confidence_interval(x_i, x_mean, ss_x, t_value, n, mse) for x_i in x]

sns.lmplot(x='YearsExperience', y='Salary', data=df)
sns.residplot(x='YearsExperience', y='Salary', data=df)
plt.plot(x, y)
plt.scatter(df['YearsExperience'], df['Salary'])
plt.plot(x, y + ci)
plt.plot(x, y - ci)
plt.show()


sns.residplot(x='YearsExperience', y='Salary', data=df)
plt.show()


df['Salary'] = df[['YearsExperience', 'Salary']].apply(lambda row: row[1] + row[0]**2 * 1000, axis=1)
plt.scatter(df['YearsExperience'], df['Salary'])
sns.regplot(x='YearsExperience', y='Salary', data=df, scatter=None, color='blue', label='order 1')
sns.regplot(x='YearsExperience', y='Salary', data=df, scatter=None, color='green', order=2, label='order 1')
plt.show()




