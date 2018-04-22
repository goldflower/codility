"""
idea: 
record max of left sub-sequence and max of right sub-sequence
then find out the max value of the sum
"""

def solution(A):
    length = len(A)
    right_max_sum = [0] * length
    left_max_sum = [0] * length
    
    for i in range(length-2, -1, -1): # right most is Z-1 < N-1
        right_max_sum[i] = max(0, right_max_sum[i+1]+A[i])
    for i in range(1, length): # left most is 1
        left_max_sum[i] = max(0, left_max_sum[i-1]+A[i])
        
    MAX = -float('inf')
    for i in range(1, length-1):
        # note that there is a gap between left and right 
        MAX = max(MAX, left_max_sum[i-1] + right_max_sum[i+1])
        
    return MAX
    
    