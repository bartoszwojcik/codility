import time

# FrogJmp (Easy)

def solution(X, Y, D):
    distance = Y - X
    return distance // D + (distance % D > 0)


if __name__ == "__main__":
    start = time.time()
    print(solution(10, 85, 30))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(1, 1000000000 , 3))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(0, 5, 1))
    end = time.time()
    print(end - start)
