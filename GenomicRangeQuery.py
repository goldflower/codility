"""
1. count cumulative sum for each char
   for example, CAGCCTA => [[0,0,1,1,1,1,1,2],
                            [0,1,1,1,2,3,3,3],
                            [0,0,0,1,1,1,1,1],
                            [0,0,0,0,0,0,1,1]]
2. if difference > 0, means the corresponding char in this sub string
"""

def solution(S, P, Q):
    # write your code in Python 3.6
    occur_times_matrix = [[0] for _ in range(4)]
    counts = [0, 0, 0, 0]
    ACG_index_map = {'A':0, 'C':1, 'G':2, 'T':3}
    ans = []
    for i, s in enumerate(S):
        if s == 'A':
            counts[0] += 1
        if s == 'C':
            counts[1] += 1
        if s == 'G':
            counts[2] += 1
        if s == 'T':
            counts[3] += 1
        for j in range(4):
            occur_times_matrix[j].append(counts[j])
    for start, end in zip(P, Q):
        for i in range(4):
            if occur_times_matrix[i][end+1] - occur_times_matrix[i][start] > 0:
                ans.append(i+1)
                break
    return ans