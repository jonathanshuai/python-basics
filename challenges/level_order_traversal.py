class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n_1 = Node(1)
n_2 = Node(2)
n_3 = Node(3)
n_4 = Node(4)
n_5 = Node(5)
n_6 = Node(6)
n_7 = Node(7)
n_8 = Node(8)
n_9 = Node(9)

n_1.left = n_2
n_1.right = n_3
n_2.left = n_4
n_2.right = n_5
n_3.left = n_6
n_6.right = n_8
n_3.right = n_7
n_7.right = n_9

"""
    1
  /   \
 2     3
/ \   / \
4  5 6   7
      \   \
       8   9
"""

def get_max_depth(node):
    if node is None:
        return -1
    return max(get_max_depth(node.left), get_max_depth(node.right)) + 1


def find_depths(node, current_depth, node_depths):
    if node is None:
        return

    node_depths[current_depth].append(node.value)
    find_depths(node.left, current_depth + 1, node_depths)
    find_depths(node.right, current_depth + 1, node_depths)

def level_order_traversal(root):
    max_depth = get_max_depth(root)
    node_depths = [[] for _ in range(max_depth + 1)]
    find_depths(root, 0, node_depths)

    for depth, nodes_at_depth in enumerate(node_depths):
        print(f'------{depth}------')
        print(" ".join(map(str, nodes_at_depth)))



level_order_traversal(n_1)