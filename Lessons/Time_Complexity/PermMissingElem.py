import time

# PermMissingElem (Easy)

def solution(A):
    test_array = [1 for i in range(len(A) + 1)]
    for i, v in enumerate(A):
        test_array[v - 1] = 0
    for i, v in enumerate(test_array):
        if v > 0:
            return i + 1


if __name__ == "__main__":
    B = [1, 10, 4, 5, 6, 7, 8, 9, 2]
    C = [2, 3, 1, 5]

    start = time.time()
    print(solution(B))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(C))
    end = time.time()
    print(end - start)
