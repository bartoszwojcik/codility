import time

# MinAvgTwoSlice (Medium)

def solution(A):

    def average(a_list):
        return sum(a_list) / len(a_list)

    min_position = -1
    min_avg = 10001
    length_a = len(A)

    for i in range(length_a - 1):
        current_avg = average(A[i:i + 2])
        if current_avg < min_avg:
            min_avg = current_avg
            min_position = i

        if i < (length_a - 2) \
                and A[i] < A[i + 1] \
                and average(A[i:i + 3]) < min_avg:
            min_avg = average(A[i:i + 3])
            min_position = i

    return min_position


if __name__ == "__main__":
    start = time.time()
    print(solution([4, 2, 2, 5, 1, 5, 8]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([0, 0]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([4, 2, 2, 5, 1, 5, 8, 678, 12, 1, 3, 53, 2, 1, 78, 85, 1]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([4, 2, 2, 5, 1, 5, 8, -1, -1, -236, 2, 363, 32, -145, 23]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([3532, 0, 1133, 0, 6326, 4631, 4622]))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution([-3, -5, -8, -4, -10]))
    end = time.time()
    print(end - start)
