import math
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
        
    def binary_search(self, keys, key):
        i = 0
        length = len(keys)
        j = length
        if key < keys[0]:
            return 0
        elif key > keys[length-1]:
            return j
        
        while i<=j:
            m = math.floor((j-i)/2 + i)
            value = keys[m]
            #print('begin:',i,j,m, value, keys[m+1])
            if key == value:
                return m
            elif key < value:
                if m>=1 and key>=keys[m-1]:
                    return m
                #print('less')
                j = m-1
            else:
                if m < length-1 and key<=keys[m+1]:
                    return m+1
                #print('more')
                i = m+1
        
        
    def insert_non_full(self, node, key):
        if node.is_leaf():
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
                
        if len(node.children[index].keys) == 2*self.t - 1:
            left_node, right_node, new_key = self.split(node.children[index])
            node.keys.insert(index, new_key)
            node.children[index] = left_node
            node.children.insert(index+1, right_node)
            if key > new_key:
                index += 1
            
        self.insert_non_full(node.children[index], key)
    
    def split(self, node):
        left_node = Node(
            keys=node.keys[:len(node.keys)//2],
            children=node.children[:len(node.children)//2+1]
        )
        right_node = Node(
            keys=node.keys[len(node.keys)//2:],
            children=node.children[len(node.children)//2:]
        )
        key = right_node.keys.pop(0)
        return left_node, right_node, key
            
        
    def insert(self, key):
        if not self.root:
            self.root = Node(keys = [key])
            return
        
        if len(self.root.keys) == 2*self.t -1:
            left_node, right_node, new_key = self.split(self.root)
            self.root = Node(keys = [new_key], children=[left_node, right_node])

        self.insert_non_full(self.root, key)
        
        
    def insert_multiple(self, keys):
        for key in keys:
            self.insert(key)
			
	def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False
        
        return self.search(node.children[index], term)

# We have initialized a sample BTree for you.
btree = BTree(4)
b_node = Node(keys=[8, 16])
b_node.children.append(Node(keys=[2, 3, 5, 7]))
b_node.children.append(Node(keys=[9, 10, 11, 12]))
b_node.children.append(Node(keys=[17, 20, 44]))
btree.root = b_node

for key in [1, 4, 6 ,-1, 13, 22]:
    btree.insert(key)
    
child_keys = btree.root.children[1].keys


# `csv` and `BTree` are given to you.
btree = BTree(5)

class NodeKey:
    def __init__(self, key=None, value=Node):
        self.key = key
        self.value = value
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key
        return self.key == other
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.key > other.key
        return self.key > other
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.key < other.key
        return self.key < other
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.key >= other.key
        return self.key >= other
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.key <= other.key
        return self.key <= other
    
    def __repr__(self):
        return "<NodeKey {k}:{v}".format(k=self.key, v=self.value)
    
with open('amounts.csv', mode='r') as f:
    reader = csv.reader(f)
    next(reader)
    
    nodekeys = [NodeKey(float(row[0]), float(row[0])) for row in reader]

btree = BTree(5)
btree.insert_multiple(nodekeys)

search = btree.search(btree.root, 17116)

root_key = btree.root.keys[0].key

class BTreeIndex(BTree):
    def search(self, node, term):
        if not self.root:
            return None
        index = 0
        for key in node.keys:
            if key == term:
                return key.value
            if term > key:
                index += 1
        if node.is_leaf():
            return None
        return self.search(node.children[index], term)

index = BTreeIndex(5)
index.insert_multiple(nodekeys)

search_1 = index.search(index.root, 171116)
search_2 = index.search(index.root, 100000000)
    