class BTreeIndex(BaseBTreeIndex):
    def greater_than(self, node, term, upper_bound=None, inclusive=False):
        if not self.root or (upper_bound and upper_bound < term):
            return []
        values = []
        for i, key in enumerate(node.keys):
            if key > term:
                if (inclusive and upper_bound and key <= upper_bound) or \
                   (not inclusive and upper_bound and key < upper_bound) or \
                    (not inclusive and not upper_bound):
                    if node.is_leaf():
                        values += [key]
                    else:
                        values +=  [key] + self.greater_than(node.children[i+1], term, upper_bound, inclusive)
            elif key == term and inclusive:
                if node.is_leaf():
                    values += [key]
                else:
                    values +=  [key] + self.greater_than(node.children[i+1], term, upper_bound, inclusive)
            else:
                if not node.is_leaf():
                    values += self.greater_than(node.children[i+1], term, upper_bound, inclusive)
        return values
        
#nodekeys = [NodeKey(r,r) for r in range(100)]        

index = BTreeIndex(5)
index.insert_multiple(nodekeys)

greater = index.greater_than(index.root,170361)
upper = index.greater_than(index.root,170361, 171409)
inclusive = index.greater_than(index.root,170361, 171409, True)


