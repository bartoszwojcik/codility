import time

# MaxProductOfThree (Easy)

def solution(A):

    A.sort()

    if A[-1] <= 0 or A[0] >= 0:
        return A[-1] * A[-2] * A[-3]

    # Condition possibly not needed anymore
    elif A[-1] >= 0 > A[-2]:
        return A[0] * A[1] * A[-1]

    elif A[0] < 0 and A[1] < 0:
        lowest = (A[0] + A[1]) * -1
        if lowest > A[-1] + A[-2] or lowest > A[-2] + A[-3]:
            return A[0] * A[1] * A[-1]

    return A[-1] * A[-2] * A[-3]



if __name__ == "__main__":
    start = time.time()
    print(solution([-3, 1, 2, -2, 5, 6]))   # 60
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([-5, 5, -5, 4])) # 125
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([-5, -5, -5, -4, 2]))    # 50
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([2, 100, 3, -1000])) # 600
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([-5, -6, -4, -7, -10]))  # -120
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([4, 7, 3, 2, 1, -3, -5]))  # 105
    end = time.time()
    print(end - start)
