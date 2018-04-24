def solution(A):
    length = len(A)
    peaks = [0] * length
    prefix_peaks_sum = [0] * (length+1)
    for i in range(1, length-1):
        if A[i] > max(A[i-1], A[i+1]):
            peaks[i] = 1
        prefix_peaks_sum[i+1] = prefix_peaks_sum[i]+peaks[i]
    prefix_peaks_sum[-1] = prefix_peaks_sum[-2]
    
    valid_partition = []
    for i in range(1, length+1):
        if length % i == 0:
            valid_partition.append(i)
    
    for v in valid_partition:
        contain_peak = True
        block = 0
        while contain_peak:
            if v * (block+1) > length:
                break
            if prefix_peaks_sum[v*block] - prefix_peaks_sum[v*(block+1)] == 0:
                contain_peak = False
            block += 1
        if contain_peak:
            return length // v
    return 0