class Queqe:
    def __init__(self):
        self.items =[]

    def Enqueqe(self, item):
        self.items.insert(0, item)

    def is_empty(self):
        return len(self.items) == 0
    
    def Dequeqe(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Dequeqe from empty queqe")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty queqe")
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
s1 = Queqe()
s1.Enqueqe(10)      
s1.Enqueqe(20)
s1.Enqueqe(30)
print(s1.display())  # Output: [30, 20, 10]
print(s1.Dequeqe())
print(s1.peek())
print(s1.size())
