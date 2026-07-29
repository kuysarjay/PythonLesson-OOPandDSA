# Searching algorithms are used to locate a specific element within a data structure, such as an array, list, or tree.
    # They are used for efficiently retrieving information in large datasets.

import bisect  
a = [2, 4, 6, 8, 10]

# Linear search using 'in'
print(6 in a)       

# Linear search using 'count'
print(a.count(7) > 0)   

# Binary search using bisect
pos = bisect.bisect_left(a, 8)
print("Found at index:", pos)