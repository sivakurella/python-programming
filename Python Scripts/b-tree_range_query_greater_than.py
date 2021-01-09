class BTreeIndex(BaseBTreeIndex):
    def greater_than(self, node, term, upper_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if upper_bound is not None:
                if inclusive and key == upper_bound:
                    values.append(key)
                if key >= upper_bound:
                    break
            if term > key:
                index += 1
                continue
            if inclusive and key == term:
                values.append(key)
            if key > term:
                values.append(key)
            if not node.is_leaf():
                values += self.greater_than(
                    node.children[index],
                    term,
                    upper_bound,
                    inclusive
                )
            index += 1
        if not node.is_leaf():
            values += self.greater_than(
                node.children[index],
                term,
                upper_bound,
                inclusive
            )
        return values
		
	def less_than(self, node, term, lower_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if lower_bound is not None:
                if inclusive and key == lower_bound:
                    values.append(key)
                if key < lower_bound:
                    index += 1
                    continue
            if inclusive and key == term:
                values.append(key)
            if key < term:
                values.append(key)
            if not node.is_leaf():
                values += self.less_than(
                    node.children[index],
                    term,
                    lower_bound,
                    inclusive
                )
            index += 1
                
        if not node.is_leaf() and key <= term:
            values += self.less_than(
                node.children[index],
                term,
                lower_bound,
                inclusive
            )
        return values
        
#nodekeys = [NodeKey(r,r) for r in range(100)]        

index = BTreeIndex(5)
index.insert_multiple(nodekeys)

greater = index.greater_than(index.root,170361)
upper = index.greater_than(index.root,170361, 171409)
inclusive = index.greater_than(index.root,170361, 171409, True)


