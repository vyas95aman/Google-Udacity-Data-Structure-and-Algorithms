list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

def bubblesort(list):
    # for whole array, i should be in range len(list)
    for i in range(3):
        for j in range(len(list) - 1 - i):
            # We do list - 1 - i, because it is one less than the length of the list. range = 0:9, - 1 = 0:8, then we compare j and j + 1 
            if (list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

print(bubblesort(list))