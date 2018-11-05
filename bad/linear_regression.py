import numpy as np
from sklearn.linear_model import LinearRegression

class MyLinearRegression():
    def __init__(self, learning_rate=1e-2, epsilon=1e-7):
        self.learning_rate = learning_rate
        self.epsilon = epsilon

    def fit(self, X, y):
        self.X = X
        self.y = y

        assert (X.shape[0] == y.shape[0])

        self.theta = np.random.randn(X.shape[1], 1)
        self.intercept = np.random.randn()

        # Initialize loss for current parameters
        fx = self.predict(self.X)
        previous_loss = 0
        current_loss = self.mse(fx)
        delta_loss = current_loss

        n_iters = 0;
        # Repeat until convergence is met
        while delta_loss > self.epsilon:
            n_iters += 1
            # Do gradient descent step
            self.gradient_descent(fx)
            fx = self.predict(self.X)

            # Calculate new loss
            previous_loss = current_loss
            current_loss = self.mse(fx)
            delta_loss = previous_loss - current_loss

        print(n_iters)

    def predict(self, X):
        assert X.shape[1] == self.theta.shape[0]
        return np.dot(X, self.theta) + self.intercept


    def gradient_descent(self, fx):
        diff = fx - self.y
        grad = np.dot(self.X.T, diff)
        # print(grad)
        self.theta -= self.learning_rate * np.dot(self.X.T, diff)
        self.intercept -= self.learning_rate * np.sum(diff)

    def mse(self, fx):
        return np.mean((fx - self.y) ** 2)

m = 5
p = 2

np.random.seed(1)
X = np.random.randn(m, p)
X.sort(0)
y = np.random.randn(m, 1)
y.sort(0)

mlr = MyLinearRegression()
mlr.fit(X, y)
mlr_predictions = mlr.predict(X)
print(mlr_predictions)
print(mlr.theta)


X[:, 1] *= 100
mlr = MyLinearRegression(learning_rate=1e-5)
mlr.fit(X, y)
mlr_predictions = mlr.predict(X)
print(mlr_predictions)
print(mlr.theta)

lr = LinearRegression()
lr.fit(X, y)
lr_predictions = lr.predict(X)
print(lr_predictions)