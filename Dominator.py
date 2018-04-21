def solution(A):
    # write your code in Python 3.6
    threshold = len(A) // 2
    d = {}
    for index, i in enumerate(A):
        d[i] = d.get(i, 0) + 1
        if d[i] > threshold:
            return index
    return -1