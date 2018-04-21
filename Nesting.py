
def solution(S):
    # write your code in Python 3.6
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