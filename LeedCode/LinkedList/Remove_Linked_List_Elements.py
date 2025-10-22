class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        data = input()
        while data != -1:
            newnode = Node(data)
            if not self.head:
                self.head = newnode
                return 

            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = newnode
            data = input()

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next 

    def remove(self, val):
        if not self.head:
            return 
        while self.head and self.head.data == val:
            self.head = self.head.next
        prev = self.head
        current = self.head
        while current:
            if current.data == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next



sll = LinkedList()
sll.insert()
sll.print()
n = int(input("\nEnter number that you want to remove from linkedlist: \n"))
sll.remove(n)

sll.print()