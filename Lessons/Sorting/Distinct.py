import time

# Distinct (Easy)

def solution(A):
    if not A:
        return 0
    A.sort()
    counter = 1
    for i, v in enumerate(A):
        if i < len(A) - 1 and v != A[i + 1]:
            counter += 1

    return counter


if __name__ == "__main__":
    start = time.time()
    print(solution([2, 1, 1, 2, 3, 1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([1, 1, 1, 1, 1, 1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([]))
    end = time.time()
    print(end - start)
