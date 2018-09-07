import time

# CyclicRotation (Easy)

def solution(A, K):
    if len(A) == 0:
        return []
    move = K % len(A)
    if move == 0:
        return A
    else:
        return A[len(A) - move:] + A[0:len(A) - move]


if __name__ == "__main__":
    start = time.time()
    print(solution([1, 2, 3], 2))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([3, 8, 9, 7, 6], 3))
    end = time.time()
    print(end - start)
