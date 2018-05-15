

def selection_sort(L):
    for index in range(len(L)):
        # shorten the list after every iteration
        small = L[index:]
        # get index of the smallest value in the shortened list
        index_min = L.index(min(small))
        # get the smallest value and the value at the current index
        minimum = L[index_min]
        current = L[index]
        # swap their indexes
        L[index] = minimum
        L[index_min] = current
    return L


assert selection_sort([9, 2, 1, 11]) == [1, 2, 9, 11]
