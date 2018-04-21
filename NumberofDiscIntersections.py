"""
1. look every boundary as a point with 0(in region), 1(out of region) 
   (e.g., for A[1]=3 => (1-3, 0), (1+3, 1))
2. sorted(1., key=lambda x: (x[0], x[1])
   for example, (0,0), (1,1), (1,0), (3,1),
   we need to add the intersection first, so we need to put 0 before 1
   when x[0]'s are the same
3. iterate, if meet 0, means get in a region, else means get out of region
"""

def solution(A):
    # write your code in Python 3.6
    points = []
    for i, j in enumerate(A):
        points.append((i-j, 0))
        points.append((i+j, 1))
    points.sort(key=lambda x: (x[0], x[1]))
    
    in_nb_regions = 0
    nb_intersects = 0
    for i, j in points:
        if j == 0:
            nb_intersects += in_nb_regions
            in_nb_regions += 1
            if nb_intersects > 10000000:
                return -1
        else:
            in_nb_regions -= 1
    return nb_intersects
        