"""
https://codility.com/media/train/solution-flags.pdf

idea:
i flags, if we set a flag at position p,
then the next flag can only be set in positions >= p + i
"""
import math

def next_peak(peaks):
    length = len(peaks)
    next_peak_pos = [0] * length
    next_peak_pos[-1] = -1
    for i in range(length-2, -1, -1):
        if peaks[i]:
            next_peak_pos[i] = i
        else:
            next_peak_pos[i] = next_peak_pos[i+1]
    return next_peak_pos

def solution(A):
    length = len(A)
    peaks = [False] * length
    
    for i in range(1, length-1):
        if A[i] > max(A[i-1], A[i+1]):
            peaks[i] = True
    next_peak_pos = next_peak(peaks)
    
    MAX = 0
    # we check how many flags i can we put on the peaks
    i = 1 # at least 1 flag
    while (i-1)*i <= length: # i <= N/i + 1
        p_this_round = 0
        cumulate_flags = 0
        while p_this_round < length and cumulate_flags < i:
            p_this_round = next_peak_pos[p_this_round]
            if p_this_round == -1:
                break
            cumulate_flags += 1
            p_this_round += i # distance between flags = i
        MAX = max(MAX, cumulate_flags)
        i += 1
    return MAX