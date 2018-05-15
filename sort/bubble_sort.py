''' Bubble sort is inefficient.

When To Use:
    - when your data is almost sorted.
    - parallelism can be exploited to speed up the  bubbling.
    - you only have a few thousand bytes of RAM
'''


def bubble_sort(L):
    for j in range(len(L)):
        # iterate from last element to the element at index j
        for i in range(len(L)-1, j-1, -1):
            if i > 0:
                right = L[i]
                left = L[i-1]
                # if the value on the right is smaller than that of the left, then swap indices
                if right < left:
                    L[i-1] = right
                    L[i] = left
    return L 


assert bubble_sort([9, 3, 4, 1, 5, 6, 8, 10]) == [1, 3, 4, 5, 6, 8, 9, 10]
