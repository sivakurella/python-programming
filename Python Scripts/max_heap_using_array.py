# We don't need to use the `Node` class anymore.
import math

class MaxHeap:
    def __init__(self):
        self.nodes = []
    
    # Add your new `insert` method here.
    def insert(self, value):
        if len(self.nodes) == 0:
            self.nodes.append(value)
        elif self.nodes[-1] > value:
            self.nodes.append(value)
        else:
            self.nodes.append(value)
            found=False
            index = len(self.nodes) - 1
            while not found:
                parent_index = math.floor((index-1)/2)
                parent_value = self.nodes[parent_index]
                if parent_value < value:
                    temp = self.nodes[parent_index]
                    self.nodes[parent_index] = value
                    self.nodes[index] = temp
                    index = parent_index
                elif parent_value >= value:
                    found=True
                
                if index == 0:
                    found = True

                    
values = [3, 9, 11]
heap = MaxHeap()

for value in values:
    print('insert a value:{}'.format(value))
    heap.insert(value)

nodes = heap.nodes
