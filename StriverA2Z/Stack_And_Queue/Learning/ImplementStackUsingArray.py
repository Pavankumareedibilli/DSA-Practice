class stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    

s = stack()
s.push(1)
s.push(2)
s.push(2)
s.display()
s.pop()
s.display()
s.size()
print(s.peek())
        