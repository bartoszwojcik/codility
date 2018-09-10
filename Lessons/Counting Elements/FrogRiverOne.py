import time

# FrogRiverOne (Easy)

def solution(X, A):
    if X > len(A):
        return -1

    places = [0 for v in range(len(A) + 1)]
    counter = X

    for index, second in enumerate(A):
        if places[second] == 0:
            places[second] = 1
            counter -= 1
        if counter == 0:
            return index

    return -1


if __name__ == "__main__":
    start = time.time()
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(5, [1, 3, 1, 4, 2, 3, 1, 4]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(10, [1, 3, 1, 4, 2, 3, 5, 4, 8, 7, 7, 7, 1, 6, 9, 2, 10]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(10, []))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(10, [1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(3, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
    end = time.time()
    print(end - start)
