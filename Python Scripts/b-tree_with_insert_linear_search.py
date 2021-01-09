class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None
        
    def insert(self, key):
        # `insert` is given to you.
        self.insert_non_full(self.root, key)

# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 16])
b_node.children.append(Node(keys=[2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node
class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def insert(self, key):
        # `insert` is given to you.
        self.insert_non_full(self.root, key)
    
    def insert_non_full(self, node, key):
        if node.is_leaf():
            if len(node.keys) >= 2*self.t - 1:
                # If it will exceed the maximum
                # don't add the key.
                return
            
            index = 0
            for k in node.keys:
                if key > k: index += 1
                else: break
            node.keys.insert(index, key)
            return
        
        index = 0
        for k in node.keys:
            if key > k: index += 1
            else: break
        self.insert_non_full(node.children[index], key)
            
# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 16])
b_node.children.append(Node(keys=[2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node
btree.insert(1)
btree.insert(4)
btree.insert(6)
btree.insert(-1)
btree.insert(13)
btree.insert(22)
child_keys = btree.root.children[1].keys