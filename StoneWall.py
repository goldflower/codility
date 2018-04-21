"""
idea: record increasing sequences
1. when increasing or empty: nb_blocks += 1
2. when decreasing: pop stack until non-decreasing
3. same: pass
"""
def solution(H):
    # write your code in Python 3.6
    block_stack = []
    nb_blocks = 0
    for h in H:
        while len(block_stack) != 0:
            if h < block_stack[-1]:
                block_stack.pop()
            else:
                break
        if len(block_stack) == 0:
            block_stack.append(h)
            nb_blocks += 1
        elif h == block_stack[-1]:
            continue
        elif h > block_stack[-1]:
            block_stack.append(h)
            nb_blocks += 1
        else:
            print("???")
    return nb_blocks