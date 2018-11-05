def rotated_binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2

        # If we found the value, return it
        if array[mid] == value:
            return mid

        # Otherwise, if the value is greater than mid...
        if array[mid] < value:
            # If array[low] is < array[mid] then value is increasing from low to mid
            if array[low] <= array[mid] or array[low] > value:
                # Look in the right side, because we're trying to find value greater than mid
                low = mid + 1
            else:
                # Otherwise, look in the left side
                high = mid

        # If the value is less than mid...
        if array[mid] > value:
            # If array[high] > array[mid], then value is increasing from mid to high.
            if array[high] >= array[mid] or array[high] < value:
                # Look in the left side because we're trying to find a vlue less than mid
                high = mid
            else:
                # If it's not increasing on the right side or the rightmost value < value
                low = mid + 1

    if array[low] == value:
        return low

    return -1



# 3, 4, 5, 1, 2
a = [5,6,7,1,2,3,4]
b = [1,2,3,4,5]
c = [2,3,1]

for val in a:
    assert rotated_binary_search(a, val) == a.index(val)

for val in b:
    assert rotated_binary_search(b, val) == b.index(val)

for val in c:
    assert rotated_binary_search(c, val) == c.index(val)

