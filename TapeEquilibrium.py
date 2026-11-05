def solution(A):
  total = sum(A)
  left = 0
  min_diff = float('inf')

for i in range(len(A) - 1): 
  left += A[i]
  right = total - left 
diff = abs(left - right 
