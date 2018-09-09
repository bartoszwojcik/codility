import time

# PermCheck (Easy)

def solution(A):
    count_array = [0 for v in range(len(A) + 1)]
    for element in A:
        try:
            count_array[element] += 1
        except IndexError:
            return 0
    for index, element in enumerate(count_array):
        if index > 0 and element != 1:
            return 0

    return 1


if __name__ == "__main__":
    start = time.time()
    print(solution([4, 1, 3, 2]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([4, 1, 3, 2, 2]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([4, 1, 2]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(
        [4, 1, 3, 2, 5, 8, 7, 6, 9, 12, 13, 14, 11, 10, 15, 17, 16]
    ))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([2053333, 2053334, 2053335]))
    end = time.time()
    print(end - start)
