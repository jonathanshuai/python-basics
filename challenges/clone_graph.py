# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        
        node_stack = [] # stack for DFS
        cache = dict() # node_label: reference to the node
        root_label = node.label
        
        
        new_node = UndirectedGraphNode(node.label)
        cache[node.label] = new_node
        node_stack.append(node) # start at the root
        
        
        while len(node_stack) > 0:
            # Pop a node to copy from the stack
            original_node = node_stack.pop()
            label = original_node.label
            
            # Create a new node from this original_node
            node_copy = cache[label]
            
            # Now, we should populate the neighbors list 
            for neighbor_node in original_node.neighbors:
                neighbor_label = neighbor_node.label
                # If the neighbor label is not in the cache
                if not neighbor_label in cache:
                    neighbor_copy = UndirectedGraphNode(neighbor_label)
                    cache[neighbor_label] = neighbor_copy
                    node_stack.append(neighbor_node)
                # If the neighbor label is in the cache
                else:
                    neighbor_copy = cache[neighbor_label]
                
                # Update this node's neighbors
                node_copy.neighbors.append(neighbor_copy)
                
        return cache[root_label]