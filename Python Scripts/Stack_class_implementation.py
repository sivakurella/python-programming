class Stack():
    def __init__(self, items=[]):
        self.items = list(items)
        
    def push(self, value):
        self.items.insert(0,value)
        
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return None
    
    def count(self):
        return len(self.items)
    
    def __str__(self):
        return self.items.__str__()
    

    
stack = Stack()
for x in range(1,4):
    stack.push(x)
stack.pop()
print(stack.items)
