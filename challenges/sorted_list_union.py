def union_sorted_lists(a, b):
    # Creating an empty combined list
    combined_list = []    
    
    # Initializing the cursors for each list 
    a_cursor = 0
    b_cursor = 0

    # Save the lengths of each list
    len_a = len(a)
    len_b = len(b)

    # While we still have elements in each array...
    while a_cursor < len_a and b_cursor < len_b:
            # Compare the values in each list at the cursors
            # And we append the value that is smaller to the combined list
            if a[a_cursor] < b[b_cursor]:
                # We only append if the value was not already in the list 
                # (since we're appending elements in a sorted order, if the value is in the list, it must be the last element)
                if combined_list == [] or combined_list[-1] != a[a_cursor]:
                    combined_list.append(a[a_cursor])

                # Continue on in that list
                a_cursor += 1

            else:
                if combined_list == [] or combined_list[-1] != b[b_cursor]:
                    combined_list.append(b[b_cursor])

                b_cursor += 1
                
    
    while a_cursor < len_a:
        if combined_list == [] or combined_list[-1] != a[a_cursor]:
            combined_list.append(a[a_cursor])

        a_cursor += 1

    while b_cursor < len_b:
        if combined_list == [] or combined_list[-1] != b[b_cursor]:
            combined_list.append(b[b_cursor])

        b_cursor += 1
        
    return combined_list



a = [1,2,3,4,5]
b = [3, 5, 6, 8]

union_sorted_lists(a, b)