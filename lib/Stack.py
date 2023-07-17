class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        if self.isEmpty != True and len(self.items) > 0:
            return self.items.pop() 
    
    def peek(self):
        if self.isEmpty():
            return 0
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return len(self.items) == 0
    
    def full(self):
        if len(self.items) >= self.limit:
            return True
        return False
    
    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1