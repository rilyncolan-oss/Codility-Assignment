def solution(A):
    ##Find the total sum of all the numbers in the array 
    total = sum(A)
    #Start the left side at 0
    left = 0
    #Keep track of the smallest difference found
    min_diff = float('inf')

    #Check each possible position where the array can be split 
    for i in range(len(A) - 1): 
        #Add the current number to the left side 
        left += A[i]

        #Calculate the sum of the right side 
        right = total - left 

        #Find the absolute difference between the two sides 
        diff = abs(left - right)

        #Update the smallest difference if this one is smaller
        min_diff = min(min_diff, diff) 

#Return the smallest difference found 
return min_diff
