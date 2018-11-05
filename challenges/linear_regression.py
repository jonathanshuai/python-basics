import numpy as np


class LR():
    def __init__(self):
        pass

    def fit(self, X, y, learning_rate=1e-3, epsilon=1e-7):
        X = np.hstack([np.ones((X.shape[0], 1)), X])
        self.theta = np.random.randn(X.shape[1], 1)
        self.gradient_descent(X, y, learning_rate, epsilon)        


    def predict(self, datum):
        """Function to calculate prediction using our theta
        datum: nxp matrix
        """
        if datum.shape[0] + 1 == self.theta.shape[0]:
            datum = np.hstack([np.ones((datum.shape[0], 1)), datum])
        return np.dot(datum, self.theta)


    def f_prime(self, X, y):
        prediction = np.dot(X, self.theta)
        return np.dot(X.T, (prediction - y)) / X.shape[0]

    def gradient_descent(self, X, y, learning_rate, epsilon):
        old_cost = np.sum((self.predict(X) - y) ** 2)

        self.theta -= learning_rate * self.f_prime(X, y)
        
        new_cost = np.sum((self.predict(X) - y) ** 2)
        while old_cost - new_cost > epsilon:
            self.theta -= learning_rate * self.f_prime(X, y)        
            old_cost = new_cost
            new_cost = np.sum((self.predict(X) - y) ** 2)

lr = LR()

X = np.array([[7, 2, 3],
    [ 6, 5, 2],
    [ 2, 5, 7],
    [ 3, 4, 12],
    [ 2, 8, 20],
    [-1, 6, 18],
    [-2, 7, 29],
    [ -2, 5, 23],
    [ -1, 5, 16]])

y = np.array([1, 5, 6, 9, 10, 12, 16, 14, 17]).reshape(-1, 1)

lr.fit(np.array(X), np.array(y).reshape((-1, 1)))

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X, y)
clf.predict(X)