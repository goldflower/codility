"""
first, we have to know there's at most 1 leader in a sequence
1. decide which element is the possible leader (with max count)
2. if it's leader in A, goto 3., else return 0
3. iterate once to check if the leader is the leader in both sub-sequences
"""

from collections import Counter
def solution(A):
    c = Counter(A)
    max_element, max_count = c.most_common(1)[0]
    ans = 0
    if len(A) // 2 >= max_count:
        return 0
    left_count = right_count = 0
    
    for i, element in enumerate(A):
        left_length = i+1
        right_length = len(A) - i - 1
        if element == max_element:
            left_count += 1
            right_count = max_count - left_count
            if ((left_length // 2 < left_count) and
                (right_length // 2 < right_count)):
                ans += 1
    return ans
            
                
        

