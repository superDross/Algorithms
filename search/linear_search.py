

def linear_search(N, L):
    for n in L:
        if n == N:
            return n

assert linear_search(10, [1, 4, 2, 24, 90, 10, 99]) == 10
