class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "queue Underflow"
        self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "queue Underflow"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)
    

q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(3)
q.enqueue(3)
q.display()
q.dequeue()
q.display()
print(q.front())
print(q.size())
