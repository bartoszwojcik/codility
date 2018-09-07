import time

# BinaryGap (Easy)

def solution(N):
    binary_int = format(N, 'b')

    n = len(binary_int) - 2
    while n > 0:
        if "1" + "0" * n + "1" in binary_int:
            return n
        else:
            n -= 1
    return 0


if __name__ == "__main__":
    test_1 = 1041
    test_2 = 1337
    test_3 = 0

    start = time.time()
    print(solution(test_1))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(test_2))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(test_3))
    end = time.time()
    print(end - start)
