class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
        temp=self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def Remove(self, n):
        size=0
        temp=self.head
        while temp:
            size+=1
            temp=temp.next

        pos = size-n
        print(size, " ", pos)
        if pos ==0 and size==1:
            return None
        elif pos == 0:
            self.head = self.head.next
        prev=self.head
        current = self.head
        while current:
            if pos == 0:
                prev.next = current.next
                current = current.next
                pos-=1

            else:
                prev = current
                current = current.next
                pos-=1

        

sll = LinkedList()

sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)

n = int(input("Enter Position that you want to remove: "))
sll.print()
sll.Remove(n)
print("\n")
sll.print()

