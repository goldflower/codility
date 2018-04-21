
"""
cand1: e.g., [-1,2]
cand2: e.g., [ 1,2]
"""
def solution(A):
    MAX = -float('inf')
    current_sum = None
    for num in A:
        if current_sum is None:
            current_sum = num
        else:
            cand1 = num
            cand2 = current_sum + num
            current_sum = max(cand1, cand2)
        MAX = max(current_sum, MAX)
    return MAX
    