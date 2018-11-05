def called_with(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



parameter_grid = {
    'apple': [1, 2],
    'banana': ['green', 'yellow'],
    'coffee': [100, 1000, 10000]
}


def hyperparam_search(parameter_grid):

    keys = list(parameter_grid.keys())
    start = 0
    current = dict()

    _hyperparam_search(parameter_grid, keys, start, current)    

def _hyperparam_search(parameter_grid, keys, start, current):
    if start == len(keys):
        called_with(**current)
        return

    current_key = keys[start]
    for element in parameter_grid[current_key]:
        current[current_key] = element
        _hyperparam_search(parameter_grid, keys, start + 1, current)



called_with(**params)