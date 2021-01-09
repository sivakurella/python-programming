class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
    
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
    def __getitem__(self, key):
        node = self
        counter = 0
        while counter < key:
            node = node.next_node
            counter += 1
        return node
    
    def insert(self, position, value):
        new_node = Node(value)
        return_node = self
        if position == 0:
            new_node.set_next_node(self)
            return_node = new_node
        else:
            split_start = self.__getitem__(position-1)
            split_end = split_start.next_node
            
            split_start.set_next_node(new_node)
            new_node.set_next_node(split_end)
            
        return return_node
		
	def pop(self, position):
        if position == 0:
            return self, self.next_node
        else:
            split_start = self[position - 1]
            removed_node = split_start.next_node
            split_end = removed_node.next_node
            
            split_start.next_node = split_end
            return removed_node, self
        
price_1 = Node(all_prices[0])

temp_price = price_1
for _ in all_prices[1:5]:
    temp_price = temp_price.append(_)
                    
price_1 = price_1.insert(3, all_prices[5])
price_1 = price_1.insert(0, all_prices[6])
price_1 = price_1.insert(7, all_prices[7])

print(price_1[3].value)

temp_price = price_1
while temp_price is not None:
    print(temp_price.value)
    temp_price = temp_price.next_node
