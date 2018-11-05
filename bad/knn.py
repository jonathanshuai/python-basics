import numpy as np
import heapq

X = np.array([[1,2,1],
              [2,1,1],
              [5,3,2],
              [6,6,3],
              [0,-1,2]])

y = np.random.randn(5, 1)


knn = KNN(3)
knn.fit(X, y)
print(knn.predict([[1,2,0]]))