

class QuadTree():
    def __init__(self, size):
        self.size = size
        self.root = {
            'split': (size // 2, size // 2),
            'bounds': {'top': size, 'right': size, 'bottom': 0, 'left': 0},
            'upper_left': None,
            'upper_right': None,
            'lower_left': None,
            'lower_right': None,
            'parent': None
        }

    def insert(self, point):
        # Extract x and y from point
        x, y = point[0], point[1]

        # Check that it fits the bounds
        if x < 0 or x > self.size or y < 0 or y > self.size:
            raise Exception("This point is out of bounds")

        # Make recursive insert call into root node
        self.insert_recursive(x, y, self.root)

    def insert_recursive(self, x, y, node):

        # Keep track of what the next node's split and bounds will be
        split = [None, None]
        bounds = {'top': None, 'right': None, 'bottom': None, 'left': None}

        # Find the quadrant that the point belongs in
        quadrant = ''
        if y > node['split'][1]:
            quadrant = 'upper_'
            split[1] = (node['bounds']['top'] - node['split'][1]) // 2
            bounds['top'] = node['bounds']['top']
            bounds['bottom'] = node['split'][1]
        else:
            quadrant = 'lower_'
            split[1] = (node['split'][1] - node['bounds']['bottom']) // 2
            bounds['top'] = node['split'][1]
            bounds['bottom'] = node['bounds']['bottom']

        if x > node['split'][0]:
            quadrant += 'right'
            split[0] = (node['bounds']['right'] - node['split'][0]) // 2
            bounds['right'] = node['bounds']['right']
            bounds['left'] = node['split'][0]         
        else:
            quadrant += 'left'
            split[0] = (node['split'][0] - node['bounds']['left']) // 2
            bounds['right'] = node['split'][0]
            bounds['left'] = node['bounds']['left']

        # If there is nothing stored here, we can just put the point here
        if node[quadrant] is None:
            node[quadrant] = (x, y)

        # If there was a point here, turn the old point into a node, and reinsert both points
        elif isinstance(node[quadrant], tuple):
            if (x, y) == node[quadrant]:
                raise Exception("A point with this value already exists.")

            old_x, old_y = node[quadrant]
            node[quadrant] = {
                'split': split,
                'bounds': bounds,
                'upper_left': None,
                'upper_right': None,
                'lower_left': None,
                'lower_right': None,
                'parent': node
            }
            self.insert_recursive(x, y, node[quadrant])
            self.insert_recursive(old_x, old_y, node[quadrant])
    
        # Otherwise, there's a dict here (a node). We can insert the point recursively.
        else:
            self.insert_recursive(x, y, node[quadrant])

    def find(self, point):
        # Extract x and y from point
        x, y = point[0], point[1]

        # Check that it fits the bounds
        if x < 0 or x > self.size or y < 0 or y > self.size:
            raise Exception("This point is out of bounds")

        # Make recursive insert call into root node
        return self.find_recursive(x, y, self.root)


    def find_recursive(self, x, y, node):
        # Find the quadrant that the point belongs in
        quadrant = ''
        if y > node['split'][1]:
            quadrant = 'upper_'
        else:
            quadrant = 'lower_'

        if x > node['split'][0]:
            quadrant += 'right'
        else:
            quadrant += 'left'

        # If there is nothing stored here, we can just put the point here
        if node[quadrant] is None:
            return False

        # If there was a point here, turn the old point into a node, and reinsert both points
        elif isinstance(node[quadrant], tuple):
            if (x, y) == node[quadrant]:
                return True
            else:
                return False

        # Otherwise, there's a dict here (a node). We can insert the point recursively.
        else:
            return self.find_recursive(x, y, node[quadrant])



point_a = (1, 5)
point_b = (3, 5)
point_c = (8, 5)
point_d = (1, 5)


quadtree = QuadTree(16)
quadtree.insert(point_a)
quadtree.insert(point_b)
print(quadtree.find(point_a))
print(quadtree.find(point_b))
print(quadtree.find(point_c))
# quadtree.insert(point_c)
# quadtree.insert(point_d)