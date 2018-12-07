import numpy as np

class MyLinearRegression():
    def __init__(self, learning_rate=1e-2, tol=1e-7):
        self.learning_rate = learning_rate
        self.tol = tol

    def fit(self, X, y):
        self.X = X
        self.y = y

        assert self.X.shape[0] == self.y.shape[0]

        self.theta = np.random.randn(X.shape[1])
        self.intercept = np.random.randn()

        prev_error = 0
        current_error = self._error()
        delta_error = current_error
       
        while delta_error > self.tol:
            self._gradient_descent()

            prev_error = current_error
            current_error = self._error()
            delta_error = prev_error - current_error



    def predict(self, X):
        assert X.shape[1] == self.X.shape[1]
        return X.dot(self.theta) + self.intercept


    def _gradient_descent(self):
        pred = self.predict(self.X)
        l1_distance = pred - self.y

        theta_update = self.learning_rate * (self.X.T.dot(l1_distance))
        intercept_update = self.learning_rate * l1_distance.sum()

        print(theta_update)
        print(intercept_update)

        self.theta -= theta_update
        self.intercept -= intercept_update

    def _error(self):
        return np.mean((self.predict(self.X) - self.y) ** 2)

np.random.seed(0)

X = np.random.randn(25, 2)
X.sort(0)
y = np.random.randn(25) * 5
y.sort()


lr1 = MyLinearRegression(learning_rate=1e-2)
lr2 = MyLinearRegression(learning_rate=1e-2)
lr1.X = X
lr1.y = y

lr1.theta = np.random.randn(X.shape[1])
lr1.intercept = np.random.randn()

lr2.X = X.copy()
lr2.y = y.copy()
lr2.X[:, 1] *= 100

lr2.theta = lr1.theta.copy()
lr2.theta[1] /= 100
lr2.intercept = lr1.intercept

lr1._gradient_descent()
print(lr1.intercept)
lr2._gradient_descent()
print(f'lr1 theta: {lr1.theta}, lr1 intercept: {lr1.intercept}')
print(f'lr2 theta: {lr2.theta}, lr2 intercept: {lr2.intercept}')
