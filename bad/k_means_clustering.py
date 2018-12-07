import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns


class KMeans(object): 
    def __init__(self, k=3, tol=1e-4):
        self.k = k
        self.tol = tol

    def fit(self, X):
        self.data = X
        assert self.k <= self.data.shape[0], "Number of data points is fewer than the number of centroids!"

        # initialize centroids
        indices = np.random.choice(self.data.shape[0], self.k, replace=False)
        self.centroids = self.data[indices]

        distances = self._calculate_distances(self.data)

        previous_loss = 0
        current_loss = self._loss(distances)
        delta_loss = current_loss
        
        while delta_loss > self.tol:
            self._recenter_clusters(distances)
            distances = self._calculate_distances(X)
            
            previous_loss = current_loss
            current_loss = self._loss(distances)
            delta_loss = previous_loss - current_loss

    def predict(self, X):
        assert X.shape[1] == self.centroids.shape[1]

        distances = self._calculate_distances(X)
        labels = np.argmin(distances, axis=1)
        return labels

    def _loss(self, distances):
        return np.mean(distances)

    def _calculate_distances(self, X):
        distances = np.zeros((X.shape[0], self.k))

        for i in range(X.shape[0]):
            for j in range(self.k):
                distances[i, j] = self._distance(X[i], self.centroids[j])

        return distances

    def _recenter_clusters(self, distances):
        labels = np.argmin(distances, axis=1)
        for j in range(self.k):
            self.centroids[j] = np.mean(self.data[labels == j], axis=0)

    def _distance(self, a, b):
        return np.sum((a - b)**2)


sns.set_style("whitegrid")
np.random.seed(1)

mu_1 = [7, 5]
sigma_1 = [0.6, 0.6]  # 0.36, 0.36
cluster_1 = np.random.normal(mu_1, sigma_1, size=[40, 2])


mu_2 = [3, 4]
sigma_2 = [0.8, 0.6]  # 0.64, 0.36
cluster_2 = np.random.normal(mu_2, sigma_2, size=[30, 2])


mu_3 = [4, 6]
sigma_3 = [0.5, 0.3]  # 0.25, 0.09
cluster_3 = np.random.normal(mu_3, sigma_3, size=[30, 2])


X = np.vstack([cluster_1, cluster_2, cluster_3])

sns.scatterplot(cluster_1[:, 0], cluster_1[:, 1])
sns.scatterplot(cluster_2[:, 0], cluster_2[:, 1])
sns.scatterplot(cluster_3[:, 0], cluster_3[:, 1])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()


kmeans = KMeans()
kmeans.fit(X)
y = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
