"""
idea: downstream try to eat upstream
1. if upstream, put it in stack
2. if downstream, try to eat fish (via pop)
3. if stack is empty, the upstream fish is alived, lives += 1
4. the remains in stack are all downstream, add len(stack)
"""

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    lives = 0
    for f, direction in zip(A[::-1], B[::-1]):
        if direction == 0: # upstream
            stack.append(f)
        else:              # downstream
            while len(stack) != 0:
                if f < stack[-1]:
                    break
                else:
                    pop = stack.pop()
            if len(stack) == 0:
                lives += 1
                
    return lives + len(stack)
        