def create_fab(N):
    if N < 2:
        yield from range(N)
    a, b = 0, 1
    yield b
    while b < N:
        a, b = b, a + b
        yield b
    
def solution(A):
    A = [0] + A + [1]
    length = len(A)
    dist = length - 1
    
    valid_jumps = set(create_fab(length))
    leaf_locations = set(i for i in range(len(A)) if A[i])
    
    next_leaf = valid_jumps & leaf_locations
    
    num_jumps = 1
    while dist not in next_leaf:
        if len(next_leaf) == 0:
            break
        num_jumps += 1
        next_leaf = {leaf + jump 
                     for leaf in next_leaf
                     for jump in valid_jumps
                     if (leaf + jump in leaf_locations and 
                         leaf + jump <= dist)}
    if dist in next_leaf:
        return num_jumps
    return -1