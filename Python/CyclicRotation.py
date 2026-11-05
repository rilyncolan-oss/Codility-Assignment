def solution(A, K): 
    if len(A) == ): 
        return A 

    K = K % len(A)

    if K == 0:
        return A


    return A[-K:] + A[:-K]
