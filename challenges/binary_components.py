from queue import Queue

def find_largest_island(array):
    m = len(array)
    n = len(array[0])

    if m < 1 and n < 1:
        return 0
    if m == 1 and n == 1:
        return array[0][0]

    components = []
    # Queue we use for BFS to find connected components
    cell_queue = Queue()

    # Visited cells
    visited = set()
    # Try every cell as a starting point (if it hasn't been visited) 
    for starting_row in range(m):
        for starting_col in range(n):
            starting_cell = (starting_row, starting_col)

            # If we haven't seen this cell before, mark it as seen.
            if not starting_cell in visited:
                visited.add(starting_cell)

                # If cell is 1, we should look for this component size. Perform BFS
                if array[starting_row][starting_col] == 1:
                    # Put the starting cell into the queue
                    cell_queue.put(starting_cell)

                    # initialize a component size
                    current_component_size = 1

                    # perform BFS
                    while not cell_queue.empty():
                        # Remove the cell from queue
                        cell_row, cell_col = cell_queue.get()
                        

                        neighbors = [(cell_row - 1, cell_col), # Top
                                     (cell_row    , cell_col + 1), # Right
                                     (cell_row + 1, cell_col), # Bottom
                                     (cell_row    , cell_col - 1)]  # Left
                        
                        # Add neighbors
                        for neighbor_row, neighbor_col in neighbors:
                            if (neighbor_row >= 0 and neighbor_row < m       # Row is in bounds 
                                and neighbor_col >= 0 and neighbor_col < n   # Column is in bounds
                                and not (neighbor_row, neighbor_col) in visited # Neighbor hasn't been visited
                                ):
                                # If neighbor value is 1, we should increment our component size and put this neighbor 
                                # into the queue to search for other connected components
                                neighbor_value = array[neighbor_row][neighbor_col]
                                if neighbor_value == 1:
                                    current_component_size += 1
                                    cell_queue.put((neighbor_row, neighbor_col))
                                # Regardless of the value, we have visited this neighbor
                                visited.add((neighbor_row, neighbor_col))

                    components.append((current_component_size, starting_cell))

    return components, max(components)



array = [[1, 0, 0, 1, 1],
         [1, 1, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]

print(find_largest_island(array))

