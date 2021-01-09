class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    # Add `insert` method here.
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        elif not self.root.left:
            self.root.left = Node(value)
        elif not self.root.right:
            self.root.right = Node(value)
        else:
            pass
        
tree = BinaryTree(Node(value=1))

for value in [2,3,4]:
    tree.insert(value)
    
root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value