import numpy as np



def percentile(data, n):
    data = np.array(data)
    data.sort()
    

    index = data.shape[0] * n / 100
    upper_index = int(np.ceil(index))
    lower_index = int(np.floor(index))

    return np.mean([data[upper_index], data[lower_index]])





data = np.random.randint(1000, size=(5))
