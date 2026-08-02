# Heap is a complete binary tree that satisfies the heap property.
# It can be used to implement a priority queue.
# A max heap is a complete binary tree where the value of each node is greater than or equal to the
    # values of its children, and the min heap is where the value of each node is less than or
    # equal to the values of its children.
    
# Example of Heap:
import heapq
a = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(a)

# printing created heap
print ("The created heap is:", a)

# Push 4 into the heap
heapq.heappush(a, 4)

# printing modified heap
print ("The modified heap after push is:", a)

# using heappop() to pop smallest element
print ("The smallest element is:", heapq.heappop(a))