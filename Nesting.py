"""
'(' = +1, ')' = -1
if become negative in the middle, return 0
just read code for other conditions
"""
def solution(S):
    count = 0
    for s in S:
        if s == '(':
            count += 1
        elif s == ')':
            count -= 1
            if count < 0:
                return 0
    if count != 0:
        return 0
    else:
        return 1