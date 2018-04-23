"""
https://codility.com/media/train/solution-flags.pdf
"""

import math

def check(x, A, peaks):
    nb_flags = x
    index = 0
    while index < len(A) and nb_flags > 0:
        if peaks[index]:
            nb_flags -= 1
            index += x
        else:
            index += 1
    return nb_flags == 0

def solution(A):
    # write your code in Python 3.6
    peaks = [False]*len(A)
    for i in range(1, len(A)-1):
        if A[i] > max(A[i-1], A[i+1]):
            peaks[i] = True
    nb_flags = 0
    for i in range(1, len(peaks)-1):
        if not check(i, A, peaks):
            return nb_flags
        else:
            nb_flags = i
    return nb_flags