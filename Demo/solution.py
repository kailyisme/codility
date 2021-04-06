def solution(A):
    if max(A) < 1:
        return 1
    A = [x for x in A if x > 0]
    A.append(0)
    A.sort()
    for n in range(len(A)-1):
        if (A[n+1] - A[n]) > 1:
            return A[n] + 1
    return max(A) + 1