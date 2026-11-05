def solution(A):
    #Find the number of elements in the array 
    N = len(A)

    #Calculate the expected sum of numbers from 1 to N + 1
    expected_sum = (N + 1) * (N + 2) // 2

    #Calculate the actual sum of the numbers in the array
    actual_sum(A)

    #Subtract the actual sum to find the missing number 
    return expected_sum - actual_sum 
  
