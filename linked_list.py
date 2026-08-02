# Linked List is a linear data structure where elements, called nodes, are stored in a sequence.
# Each node contains two parts: the data and a reference (or link) to the next node in the sequence.
# The last node points to None, indicating the end of the list.
# Linked List allows for efficient insertions and deletions,
    # especially when elements need to be added or removed from the beginning or middle of the list,
    # as no shifting of elements is required.

# Example of Linked List:
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__=='__main__':

    # Create a linked list
    # 10 -> 20 -> 30
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    
    # Print the list
    temp = head
    while temp != None:
        print(temp.data, end = " ")
        temp = temp.next