import time

# Triangle (Easy)

def solution(A):

    if len(A) < 3:
        return 0

    A.sort()

    if A[-3] <= 0:
        return 0

    for i_1, v in enumerate(A):
        if i_1 > len(A) - 3:
            break
        elif v <= 0:
            continue

        for i_2 in range(i_1 + 1, len(A) - 1):
            if v + A[i_2] < A[i_2 + 1]:
                continue

            for i_3 in range(i_2 + 1, len(A)):
                if v + A[i_2] > A[i_3]:
                    return 1

    return 0

if __name__ == "__main__":
    start = time.time()
    print(solution([10, 2, 5, 1, 8, 20]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([2, 4]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([2, 120, 348, 1234, 11337]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([5, 3, 3]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([-2, -2, -2]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([1, 1, 2, 3, 5]))
    end = time.time()
    print(end - start)
