"""
2 situations:
1. i**2 = N => count += 1
2. i*j = N => count += 2
"""

import math
def solution(N):
    count = 0
    tmp = int(math.sqrt(N))
    for i in range(1, tmp+1):
        if N % i == 0:
            if i**2 == N:
                count += 1
            else:
                count += 2
    return count
        