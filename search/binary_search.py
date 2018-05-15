

def binary_search(N, L):
    L.sort()
    while True:
        i = len(L)//2
        centre = L[i]
        if centre == N:
            return N
        elif centre < N:
            L = L[i:]
        else:
            L = L[:i]


assert binary_search(6, [1, 9, 7, 3, 6, 10, 8]) == 6
