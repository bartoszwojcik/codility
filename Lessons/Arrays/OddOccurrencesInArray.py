import time

# OddOccurrencesInArray (Easy)

def solution(A):
    if len(A) == 1:
         return A[0]
    A.sort()
    for i in range(0, len(A), 2):
         if i + 1 == len(A):
             return A[i]
         if A[i] != A[i + 1]:
             return A[i]


if __name__ == "__main__":
    test_1 = [9, 3, 9, 3, 9, 7, 9]
    test_2 = [1, 1, 2, 2, 3]

    start = time.time()
    print(solution(test_1))
    end = time.time()
    print(end - start)

    start = time.time()
    print(solution(test_2))
    end = time.time()
    print(end - start)
