import time

# GenomicRangeQuery (Medium)

def solution(S, P, Q):

    n_dict = {
        "A": [0] * (len(S) + 1),
        "C": [0] * (len(S) + 1),
        "G": [0] * (len(S) + 1)
    }

    for i, nucleotide in enumerate(S):
        if nucleotide in ("A", "C", "G"):
            n_dict[nucleotide][i + 1] = n_dict[nucleotide][i] + 1
            for k, v in n_dict.items():
                if k != nucleotide:
                    n_dict[k][i + 1] = n_dict[k][i]
        else:
            for k, v in n_dict.items():
                n_dict[k][i + 1] = n_dict[k][i]


    results = []
    for i, v in enumerate(P):
        if n_dict["A"][v] < n_dict["A"][Q[i] + 1]:
            i_factor = 1
        elif n_dict["C"][v] < n_dict["C"][Q[i] + 1]:
            i_factor = 2
        elif n_dict["G"][v] < n_dict["G"][Q[i] + 1]:
            i_factor = 3
        else:
            i_factor = 4

        results.append(i_factor)

    return results


if __name__ == "__main__":
    start = time.time()
    S = "CAGCCTA"
    P = [2, 5, 0]
    Q = [4, 5, 6]
    print(solution(S, P, Q))
    end = time.time()
    print(end - start)

    start = time.time()
    S = "C"
    P = [0]
    Q = [0]
    print(solution(S, P, Q))
    end = time.time()
    print(end - start)

    start = time.time()
    S = "CAGCCTACAGGTACTTTAGCATAGACTAGACATAGACCCTAGTACATTTAAAAGGGACCCCATAGACAT"
    P = [2, 5, 0, 0, 13, 3, 18, 2, 3, 5, 2, 1, 2, 5, 7, 0, 0]
    Q = [4, 5, 6, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68]
    print(solution(S, P, Q))
    end = time.time()
    print(end - start)

    start = time.time()
    S = "A"
    P = [0]
    Q = [0]
    print(solution(S, P, Q))
    end = time.time()
    print(end - start)

    start = time.time()
    S = "AT"
    P = [0]
    Q = [1]
    print(solution(S, P, Q))
    end = time.time()
    print(end - start)
