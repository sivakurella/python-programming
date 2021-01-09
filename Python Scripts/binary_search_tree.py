class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
    
    def __str__(self):
        return "<Node: {}>".format(self.value)

class BST:
    def __init__(self):
        self.node = None
        
    def insert(self, value):
        node = Node(value=value)
        if not self.node:
            self.node = node
            self.node.left = BST()
            self.node.right = BST()
            return
        
        if value > self.node.value:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value)
            else:
                self.node.left.node = node
                
        # check the balance
        ldepth, rdepth = 0,0
        if self.node.left:
            ldepth = self.depth(self.node.left.node)
        if self.node.right and self.node.right.node:
            rdepth = self.depth(self.node.right.node)
        print(ldepth, rdepth, self.node.value, value)
        
        
        # right-right or right-left 
        if ldepth - rdepth <= -2:
            # now figure if its right-left or right-right case
            if value <= self.node.right.node.value:
                # right left case
                self.node.right.right_rotate()

            self.left_rotate()
                
        elif ldepth - rdepth >= 2:
            # now figure is its left-right or left-left case
            if value > self.node.left.node.value:
                # left left case
                self.node.left.left_rotate()
            self.right_rotate()
        
    def inorder(self, bst):
        if not bst or not bst.node:
            return []
        
        return self.inorder(bst.node.left) + [bst.node.value] + self.inorder(bst.node.right)
		
	def insert_multiple(self, values):
        for value in values:
            self.insert(value)
			
	def search(self, value):
        if not self.node:
            return False
        elif self.node.value == value:
            return True
        elif self.node.value > value:
            return self.node.left.search(value)
        elif self.node.value < value:
            return self.node.right.search(value)
			
	def depth(self, node):
        if not node:
            return 0
        lvalue, rvalue = 0, 0
        if node.left:
            lvalue = 1 + self.depth(node.left.node)
        if node.right:
            rvalue = 1 + self.depth(node.right.node)
            
        return max(lvalue, rvalue, 1) # adding one for the node itself
		
	def is_balanced(self):
        if not self.node:
            return True
        
        left_subtree = self.depth(self.node.left.node)
        right_subtree = self.depth(self.node.right.node)
        
        return abs(left_subtree - right_subtree) < 2
		
	def left_rotate(self):
        ldepth, rdepth = 0,0
        if self.node.left:
            ldepth = self.depth(self.node.left.node)
        if self.node.right:
            rdepth = self.depth(self.node.right.node)
            
        if rdepth - ldepth >= 2:
            mv_node = self.node
            self.node = mv_node.right.node
            
            # move the left node of the right node
            r_node = self.node.left.node
            mv_node.right.node = r_node
            
            # stitch back the old node
            self.node.left.node = mv_node
            
    def right_rotate(self):
        ldepth, rdepth = 0,0
        if self.node.left:
            ldepth = self.depth(self.node.left.node)
        if self.node.right:
            rdepth = self.depth(self.node.right.node)
            
        if ldepth - rdepth >= 2:
            mv_node = self.node
            self.node = mv_node.left.node
            
            # move the right node of the left node
            l_node = self.node.right.node
            mv_node.left.node = l_node
            
            # stitch back the old node
            self.node.right.node = mv_node
    

bst = BST()
for value in [4,2,1,5,3]:
    bst.insert(value)
    
sorted_order = bst.inorder(bst)
root = bst.node.value

bst.node.left.node.left.node.value