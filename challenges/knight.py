# ???????????? INCOMPLETE

def min_knight_moves(A, B):
    delta_x = abs(A[0] - B[0])
    delta_y = abs(A[1] - B[1])

    n_steps, new_bounds = get_reduced_problem(sorted((delta_x, delta_y)))

    if new_bounds == (0, 1):
        return n_steps + 3

    

def get_reduced_problem(bounds):
    # entry condition: x <= y
    x, y = bounds

    n_steps = min(x, y // 2)
    new_bounds = (x - n_steps, y - 2 * n_steps)
    return n_steps, sorted(new_bounds)


A = (3, 5)
B = (10, 12)