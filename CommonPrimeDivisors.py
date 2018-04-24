"""
idea:
if greatest common divisor D of A, B contains all the primes of them,
then gcd(D, A) = gcd(D, B) = 1, if not, it should be contained in D
"""
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(A, B):
    count = 0
    for i in range(len(A)):
        a, b = A[i], B[i]
        p = gcd(a, b)
        while True:
            d = gcd(a, p)
            if d == 1:
                break
            a /= d
        while True:
            d = gcd(b, p)
            if d == 1:
                break
            b /= d
        if a == 1 and b == 1:
            count += 1
    return count
            