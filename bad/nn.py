import numpy as np

np.random.seed(1)


parameters = {
    'W1': np.random.randn(6, 5) * 0.001,
    'b1': np.zeros((6,1)),
    'W2': np.random.randn(1, 6),
    'b2': np.zeros((1,1))
}

def relu(z):
    return z.clip(0)

def sigmoid(z):
    return 1 / (np.exp(-z))

def forward(x, parameters):
    cache = dict()

    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    assert x.shape[0] == W1.shape[1]

    a1 = relu(np.dot(W1, x) + b1)

    a2 = sigmoid(np.dot(W2, a1) + b2)

    cache['a1'] = a1
    
    return a2, cache

def loss(y, pred):
    return -np.sum(y * np.log(pred) + (1 - y) * np.log(1 - pred), axis=1)

def backward(output, y, parameters, cache):
    m = output.shape[1]

    assert m == y.shape[1]

    a1 = cache['a1']
    W2 = parameters['W2']
    W1 = parameters['W1']

    dA2 = - y / (output) - (1 - y) / (1 - output)
    print(dA2.shape)

    dZ2 = dA2 * output * (1 - output)
    print(dZ2.shape)

    dW2 = np.dot(dZ2, a1) / m
    db2 = dZ2.sum(axis=1, keepdims=True)
    dA1 = np.dot(W2.T, dZ2)

    dZ1 = dA1 * a1
    print(dZ2.shape)

    dW2 = np.dot(dZ2, a1) / m
    db2 = dZ2.sum(axis=1, keepdims=True)
    ???????????????????????????????????????????????????


x = np.random.randint(10, size=(5,3))
y = np.random.randint(2, size=(1,3))

output = forward(x, parameters)
print(loss(y, output))