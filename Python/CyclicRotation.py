def solution(A, K): 
    #If the array is empty, return it without making changes 
    if len(A) == ): 
        return A 

    #Make sure the number of rotations does not exceed the array length 
    K = K % len(A)

    #If no rotations are needed, return the original array 
    if K == 0:
        return A


    #Move the last K elements to the beginning of the array 
    return A[-K:] + A[:-K]
