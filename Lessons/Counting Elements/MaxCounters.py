import time

# MaxCounters (Medium)

def solution(N, A):
    counters = [0 for c in range(N)]
    max_counter = 0
    # To avoid correcting the whole list each time N + 1 is provided,
    # all_counter is set for verifying current value and providing the final
    # value for too low counters at the end. The result is O(N + M).
    all_counter = 0
    for element in A:
        if element > N:
            all_counter = max_counter
        else:
            if counters[element - 1] < all_counter:
                counters[element - 1] = all_counter
            counters[element - 1] += 1
            if counters[element - 1] > max_counter:
                max_counter += 1
    counters = [all_counter if c < all_counter else c for c in counters]
    return counters


if __name__ == "__main__":
    start = time.time()
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(5, A))
    end = time.time()
    print(end - start)
