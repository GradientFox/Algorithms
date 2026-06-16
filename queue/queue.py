class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return self.size() == 0
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        response = self.items[0]
        del self.items[0]
        return response
    