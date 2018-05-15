

def insertion_sort(L):
    while True:
        change = 0
        for index in range(len(L)-1):
            current = L[index]
            next_value = L[index+1]
            if next_value < current:
                L[index] = next_value
                L[index+1] = current
                change += 1
        if change == 0:
            return L


assert insertion_sort([10, 1, 5, 2]) == [1, 2, 5, 10]
