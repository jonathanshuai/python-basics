import matplotlib.pyplot as plt

import numpy as np

from scipy.stats import norm

from sklearn.neighbors import KernelDensity


np.random.seed(1)

# X = np.random.normal(0, 1, [100, 1])
# Y = np.random.normal(0, 0.01, [100, 1])
X = [
    [-0.25],
    [0.25],
    [0.40],
]

Y = [
    [0],
    [0],
    [0],
]


x_space = np.linspace(-4, 4, 2000)

kde = KernelDensity(kernel='gaussian', bandwidth=0.1).fit(X)
log_dens = kde.score_samples(x_space.reshape([-1, 1]))
density = np.exp(log_dens)

plt.plot(x_space, density)
plt.plot(x_space, norm.pdf(x_space))
plt.scatter(X, Y, marker='+')
# plt.yaxis(0, 1)
plt.show()


class GaussianKernelDensity:
    def __init__(self, bandwidth=0.1):
        self.bandwidth = 0.1

    def fit(self, data):
        self.data = np.array(data)
        self.n = self.data.shape[0]
        return self

    def score_samples(self, x):
        return np.array([self.estimate_point(x_i) for x_i in x])

    def estimate_point(self, x_i):
        u = (self.data - x_i) / self.bandwidth
        K_u = self.kernel(u)
        return (1 / (self.n * self.bandwidth)) * np.sum(K_u)


    def kernel(self, u):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * u ** 2)

a = np.array([1, 2, 3])
b = np.array([1, 2, 5, 6])


gkde = GaussianKernelDensity().fit(X)
gkde_density = gkde.score_samples(x_space)

plt.plot(x_space, gkde_density, label='gkde_density')
plt.plot(x_space, norm.pdf(x_space))
plt.scatter(X, Y, marker='+')
# plt.yaxis(0, 1)
plt.legend()
plt.show()


# lambda x: self.kernel_function((a - x) / self.bandwidth) 