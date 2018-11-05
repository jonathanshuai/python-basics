# https://www.glassdoor.com/Interview/Facebook-Interview-RVW4842896.htm

def display_merge(a, b):
    if len(a) == 0:
        print(" ".join(map(str, b)))
        return

    if len(b) == 0:
        print(" ".join(map(str, a)))
        return

    cursor_a = 0
    cursor_b = 0

    while cursor_a < len(a) and cursor_b < len(b):
        if a[cursor_a] < b[cursor_b]:
            print(a[cursor_a], end=" ")
            cursor_a += 1

        else:
            print(b[cursor_b], end=" ")
            cursor_b += 1

    # Print the rest of a or b, whichever has remaining elements
    while cursor_a < len(a):
        print(a[cursor_a], end=" ")
        cursor_a += 1

    while cursor_b < len(b):
        print(b[cursor_b], end=" ")
        cursor_b += 1

    print()


a = [1,2,3,4,5]
b = [3, 5, 6, 8]

display_merge(a, b)