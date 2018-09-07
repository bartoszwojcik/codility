# MissingInteger (Medium)
import time

def solution(A):
    int_array = [i for i in range(1000001)]
    for element in A:
        if 1000000 >= element >= 1:
            int_array[element] = 0
    for element in int_array:
        if element != 0:
            return element
    return None


if __name__ == "__main__":

    F = [-2, -5, -1]
    B = []
    C = [1, 3, 6, 4, 1, 2]

    print(solution(F))
    print(solution(B))
    print(solution(C))

    start = time.time()
    print(solution(F))
    end = time.time()
    print(end - start)
