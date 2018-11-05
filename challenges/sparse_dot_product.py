import numpy as np
def sparse_dot_product(vector_a, vector_b):
    dot_product = 0

    if len(vector_a) != len(vector_b):
        raise ValueError(f"Vector lengths {len(vector_a)} and {len(vector_b)} do not match")
    for key in vector_a.data.keys():
        if key in vector_b.data:
            dot_product += vector_a.data[key] * vector_b.data[key]

    return dot_product

def sparse_dot_product_check(vector_a, vector_b):
    return np.dot(vector_a, vector_b)



# Example of a sparse vector
a = [0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1]
b = [0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 4, 0, 0, 0, 0, 1]
c = [0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 4, 0, 0, 0, 0, 1]


def compress_sparse_vector(a):
    return [(i, value) for i, value in enumerate(a) if value != 0]


class SparseVector:
    def __init__(self, a):
        self.data = {i: value for i, value in enumerate(a) if value != 0}
        self.length = len(a)

    def __len__(self):
        return self.length


a_compress = SparseVector(a)
b_compress = SparseVector(b)
c_compress = SparseVector(c)