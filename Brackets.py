
def solution(S):
    # write your code in Python 3.6
    stack = []
    pop_dict = {']':'[', ')':'(', '}':'{'}
    in_set = set(['[','(','{'])
    for s in S:
        if s in in_set:
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            pop = stack.pop()
            if pop != pop_dict[s]:
                return 0
    if len(stack) == 0:
        return 1
    return 0 