"""
check slice with size 2 or 3
proof:
https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf
"""

def solution(A):
    # write your code in Python 3.6
    min_index = 0
    MAX = 10001
    overall_min_mean = min_2mean = min_3mean = MAX
    for i in range(len(A)-1):
        current_min_2mean = (A[i] + A[i+1]) / 2
        try:
            current_min_3mean = (A[i] + A[i+1] + A[i+2]) / 3
        except:
            current_min_3mean = MAX
        if current_min_2mean < overall_min_mean:
            overall_min_mean = current_min_2mean
            min_index = i
        if current_min_3mean < overall_min_mean:
            overall_min_mean = current_min_3mean
            min_index = i
    return min_index