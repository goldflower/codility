
def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    last_max = 0 # update the whole counters in the end
    maybe_last_max = 0 # for possible max counter
    for operation in A:
        if 1 <= operation <= N:
            # we should involke the max operation before increasing counter
            if counters[operation-1] < last_max:
                counters[operation-1] = last_max
            counters[operation-1] += 1
            if counters[operation-1] > maybe_last_max:
                maybe_last_max = counters[operation-1]
        else:
            last_max = maybe_last_max
    for i in range(len(counters)):
        if counters[i] < last_max:
            counters[i] = last_max
    return counters