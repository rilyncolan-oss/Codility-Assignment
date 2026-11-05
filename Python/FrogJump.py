def solution(X, Y, D): 
    #Calculate the distance the frog still needs to travel 
    distance = Y - X

    #Calculate the minimum of jumos needed to reach the target 
    #Adding D - 1 makes sure we round up if there is a remainder 
    jumps = (distance + D - 1) // D 

    #Return the number of jumps 
    return jumps 
