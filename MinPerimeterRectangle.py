import math
def solution(N):
    MIN = 1e9
    tmp = int(math.sqrt(N))
    for i in range(tmp, 0, -1):
        if N % i == 0:
            return 2*(i+N//i)