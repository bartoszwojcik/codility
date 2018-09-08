import time

# TapeEquilibrium (Easy), O(N)

def solution(A):
    first_part = 0
    second_part = sum(A)
    minimum = None
    for element in A[:-1]:
        first_part += element
        second_part -= element
        distance = abs(first_part - second_part)
        if minimum is None or distance < minimum:
            minimum = distance
    return minimum


if __name__ == "__main__":
    B = [3, 1, 2, 4, 3]
    C = [0, 0]
    D = [3, 1, 2, 4, 3, -2, 10, -252, 1000, 2, 1, 0]

    start = time.time()
    print(solution(B))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(C))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(D))
    end = time.time()
    print(end - start)
