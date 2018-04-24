def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(N, M):
    div = gcd(N, M)
    return N // div