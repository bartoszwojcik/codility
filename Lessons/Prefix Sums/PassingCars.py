import time

# PassingCars (Easy)

def solution(A):
    zero_counter = 0
    pairs = 0
    for car in A:
        if car == 0:
            zero_counter += 1
        else:
            pairs += zero_counter
            if pairs > 1000000000:
                return -1
    return pairs


if __name__ == "__main__":
    start = time.time()
    print(solution([0, 1, 0, 1, 1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([0]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([1, 1, 1]))
    end = time.time()
    print(end - start)
