import numpy as np
def mat_mul(A, B):
    m_A, n_A = len(A), len(A[0])
    m_B, n_B = len(B), len(B[0])

    result = [[0] * n_B for _ in range(m_A)]

    for row_index in range(m_A):
        # Multiply this row by each column in B
        for col_index in range(n_B):
            for i in range(m_B):
                result[row_index][col_index] += A[row_index][i] * B[i][col_index]

    return result



def mat_mul_check(A, B):
    return np.dot(np.array(A), np.array(B))



A = [[1, 2, 3, 4, 6],
     [5, 6, 7, 8, 3],
     [1, 2, 3, 4, 2],
     [9, 2, 3, 3, 7]]


B = [[2, 8, 2, 4],
     [7, 3, 5, 8],
     [3, 7, 1, 6],
     [3, 2, 2, 3],
     [1, 7, 6, 4]]

