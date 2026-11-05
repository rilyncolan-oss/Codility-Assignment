def solution(A):
    #Start the result at 0 
    result = 0 

    #Go through every number in the array 
    for number in A:
        #XOR cancels out numbers that appear in pairs 
        result = result ^ number 

    #Return the number that appears an odd number of times 
    return result 
