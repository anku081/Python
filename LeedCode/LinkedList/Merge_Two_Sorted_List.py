class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        data = int(input("Enter data (-1 to stop): "))
        while data != -1:
            newnode = Node(data)
            if not self.head:
                self.head = newnode
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = newnode
            data = int(input("Enter data (-1 to stop): "))
            

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    #def MergeSorted(self):





sll = LinkedList()
sll.insert()
sll.print()