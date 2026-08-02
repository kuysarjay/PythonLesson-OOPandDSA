# Tree Data Structure is a non-linear data structure in which a collection of elements known as
    # nodes are connected to each other via edges such that there exists exactly one path
    # between any two nodes.
# Trees are used in many areas of computer science, including file systems,
    # databases and even artificial intelligence.
    
# Example of Tree Data Structure:
# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None
        
def printInorder(root):
    if(root == None):
        return
    printInorder(root.left)
    print(root.data, end = " ")
    printInorder(root.right)

if __name__ == '__main__':
    
    # Construct Binary Tree of 4 nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    
    printInorder(root)