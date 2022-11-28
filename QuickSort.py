# """Implement quick sort in Python.
# Input a list.
# Output a sorted list."""

def quicksort(array):
    size = len(array)
    for i in reversed(range(size)):
        for j in reversed(range(i - 1)):
            while array[i] < array[j]:
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = array[j]
                array[j] = temp
                print(array)
    return array


# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [33, 1, 4, 5, 24, 15, 66, 5, 0, 8, 9, 12, 25, 56, 33]
print(quicksort(test))

# for i in reversed(range(len(test))):
#     print(i)