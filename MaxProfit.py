"""
iterate once, if profit becomes negative => try another day to invest
record the best profit
"""

def solution(A):
    current_max = 0
    try_start = 0
    for i in range(len(A)):
        if A[i] - A[try_start] > current_max:
            current_max = A[i] - A[try_start]
        elif A[i] - A[try_start] < 0:
            try_start = i
    return current_max
        