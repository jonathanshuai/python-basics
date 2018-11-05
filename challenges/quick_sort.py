def make_pivot_swaps(array, low, high):
    # Pivot around high. Keep track of pivot_index, the final index to swap pivot to
    pivot_index = low

    for i in range(low, high):
        if array[i] <= array[high]:
            array[pivot_index], array[i] = array[i], array[pivot_index]
            pivot_index += 1

    array[pivot_index], array[high] = array[high], array[pivot_index]
    return pivot_index



def quick_sort(array, low, high):
    if low < high:
        pivot_index = make_pivot_swaps(array, low, high)

        quick_sort(array, pivot_index + 1, high)
        quick_sort(array, low, pivot_index - 1)


array1 = [1, 5, 2, 3, 6, 4]
array2 = [2, 7, 1, 3, 5, 4, 6, 8]

quick_sort(array1, 0, 5)
quick_sort(array2, 0, 7)