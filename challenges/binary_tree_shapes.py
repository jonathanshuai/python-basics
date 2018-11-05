def binary_tree_shapes(n_nodes):
    if n_nodes == 0:
        return 1
    if n_nodes == 1:
        return 1
    if n_nodes == 2:
        return 2

    # For each subtree (left, right), I can choose to put i btwn 0 and n_nodes-1 in that subtree
    # Furthermore, the number of subtrees that can be made with i nodes is binary_tree_shapes(i)
    # The total number of subtrees we can make with n_nodes is the sum of the number of
    # combinations for every allocation of the nodes in the left and right subtrees.

    total_subtrees = 0
    for i in range(n_nodes):  # i goes from 0 to n_nodes - 1
        left_subtrees = binary_tree_shapes(i)
        right_subtrees = binary_tree_shapes(n_nodes - 1 - i)

        combinations_i = left_subtrees * right_subtrees
        total_subtrees += combinations_i

    return total_subtrees

assert binary_tree_shapes(0) == 1
assert binary_tree_shapes(1) == 1
assert binary_tree_shapes(2) == 2
assert binary_tree_shapes(3) == 5
assert binary_tree_shapes(4) == 14
assert binary_tree_shapes(5) == 42
