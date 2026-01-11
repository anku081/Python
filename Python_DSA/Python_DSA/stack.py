class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    


class Stack:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, items):
        self.items.append(items)
        return self.items
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)

    def display(self):
        return self.items        
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.display())  # Output: [10, 20, 30]
print(s1.pop())
print(s1.peek())
print(s1.size())
print(s1.is_empty())