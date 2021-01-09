class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class MaxHeap:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        node = Node(value=value)
        if not self.root:
            self.root = node
            return node
        elif self.root.value >= value:
            if not self.root.left:
                self.root.left = node
                self.root.left.parent = self.root
            if not self.root.right:
                self.root.right = node
                self.root.right.parent = self.root
            return node
        else:
            #swap nodes
            temp = self.root
            if not self.root.left:
                self.root = node
                node.left = temp
                node.left.parent = self.root
            else:
                self.root = node
                node.right = temp
                node.right.parent = node
                node.left = temp.left
                node.left.parent =node
                temp.left = None
            return node
                
        
values = [3, 9, 11]
heap = MaxHeap()

for value in values:
    heap.insert(value)

root = heap.root.value
left = heap.root.left.value
right = heap.root.right.value