import time

# CountDiv (Medium)

def solution(A, B, K):
    if A == 0:
        return B // K + 1
    return B // K - (A - 1) // K


if __name__ == "__main__":
    start = time.time()
    print(solution(6, 11, 2))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(2, 4, 2))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(2, 2, 3))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 33, 3))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 1000, 3))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 2000000000, 3))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 5, 10))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 0, 11))
    end = time.time()
    print(end - start)

