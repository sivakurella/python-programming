class Node:
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __str__(self):
        return "<Node: {}>".format(self.value)

class BST(BaseBST):
    def __init__(self, index=None):
        self.node = None
        self.index = index
    
    # Modify `insert` and `search`.
    def search(self, key):
        if not self.node:
            return False
        
        elif self.node.key == key:
            return True
        elif self.node.key > key:
            return self.node.left.search(key)
        elif self.node.key < key:
            return self.node.right.search(key)
        
        
    def insert(self, value):
        if self.index:
            key = value[self.index]
        else:
            key = value
        node = Node(key=key, value=value)
            
        if not self.node:
            self.node = node
            self.node.left = BST(index=self.index)
            self.node.right = BST(index=self.index)
            return
        
        if key > self.node.key:
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
        
        
        # right-right or right-left 
        if ldepth - rdepth <= -2:
            # now figure if its right-left or right-right case
            if key <= self.node.right.node.key:
                # right left case
                self.node.right.right_rotate()

            self.left_rotate()
                
        elif ldepth - rdepth >= 2:
            # now figure is its left-right or left-left case
            if key > self.node.left.node.key:
                # left left case
                self.node.left.left_rotate()
            self.right_rotate()
            
            
bst = BST()
bst.insert_multiple(bst_values)
inorder = bst.inorder(bst)


bst_list = BST(index=2)
bst_list.insert_multiple(bst_list_values)
inorder_list = bst_list.inorder(bst_list)