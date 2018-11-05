
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


def get_maximum_span(node, current_distance):
    if node is None:
        return current_distance + 1, current_distance - 1

    min_span_left, max_span_left = get_maximum_span(node.left, current_distance - 1)
    min_span_right, max_span_right = get_maximum_span(node.right, current_distance + 1)

    return min(min_span_left, min_span_right), max(max_span_left, max_span_right)

def print_vertical(root):
    span_min, span_max = get_maximum_span(root, 0)
    node_levels = [[] for _ in range(span_min, span_max + 1)]
    fill_node_levels(root, node_levels, abs(span_min))

    for nodes_on_level in node_levels:
        print(" ".join(map(str, nodes_on_level)))

def fill_node_levels(node, node_levels, current_level):
    if node is None:
        return

    node_levels[current_level].append(node.value)
    fill_node_levels(node.left, node_levels, current_level - 1)
    fill_node_levels(node.right, node_levels, current_level + 1)


print_vertical(n_1)