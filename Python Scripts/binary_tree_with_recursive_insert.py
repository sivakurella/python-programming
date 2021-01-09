level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        # Helpful method to keep track of Node values.
        return "<Node: {}>".format(self.value)    

class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)
    
    # Implement your `insert` method here.
    def insert(self, values, index=0):
        node=None
        
        if index < len(values):
            node = Node(value=values[index])
            
            if not self.root:
                self.root = node
            
            node.left = self.insert(values, index=index*2+1)
            node.right = self.insert(values, index=index*2+2)
            
        return node
		
	def is_parent(self, node):
        if node.left or node.right:
            return True
        else:
            return False
    
    def is_interior(self, node):
        if (node != self.root) and self.is_parent(node):
            return True
        else:
            return False
        
    def is_leaf(self, node):
        return (node != self.root) and not self.is_parent(node)
		
	def preorder_traverse(self, node):
        if not node:
            return []
        return [node.value] + self.preorder_traverse(node.left) + self.preorder_traverse(node.right)
        
    def inorder_traverse(self, node):
        if not node:
            return []
        return self.inorder_traverse(node.left) + [node.value] + self.inorder_traverse(node.right)
    
    def postorder_traverse(self, node):
        if not node:
            return []
        return self.postorder_traverse(node.left) +  self.postorder_traverse(node.right) + [node.value]
		
	def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def num_nodes(self, node):
        return len(self.preorder_traverse(node))
		
	def is_balanced(self, node):
        if not node:
            return True
        
        return (abs(self.height(node.left) - self.height(node.right)) <= 1)  & \
    self.is_balanced(node.left) & self.is_balanced(node.right)
            
        
tree = BinaryTree(level_order)
root = tree.root.value
child = tree.root.left.right.left.value

level_order = [1, 2, 3, 4, 5]

tree = BinaryTree(level_order)

#Uncomment the following to test.
root_parent = tree.is_parent(tree.root)
parent = tree.is_parent(tree.root.left)
interior = tree.is_interior(tree.root.left)
root_leaf = tree.is_leaf(tree.root)
leaf = tree.is_leaf(tree.root.left.left)