'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
         self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp.next:
            print(temp.data, end=" ")
            temp = temp.next
        

ll = SingleLinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.print() '''







class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
    def delete(self):
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def size(self):
        temp = self.head
        size=0
        while temp:
            size+=1
            temp = temp.next
        return size

    def RemoveDuplicate(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            if prev.data == temp.data:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next

    def removeElement(self, val):
        prev = self.head
        current = self.head
        while current:
            if current.data == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
            
            

sll = SingleLinkedList()

sll.insert(1)
sll.insert(2)
sll.insert(6)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.insert(6)

sll.print()  
print("\n")
print("Size fo Linked List: ", sll.size())
#sll.delete()\
#sll.RemoveDuplicate()
sll.removeElement(6)
print("\n")
sll.print()  
