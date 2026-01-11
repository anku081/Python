### Single Linked List Implementation in Python
class LinkedlinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlink:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = LinkedlinkNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end= "->")
            current = current.next
        print("None")

    def FindLowest(self):
        if self.head is None:
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
            return min_value
        
    def max_element(self):
        if self.head is None:
            return None
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value



l1 = Linkedlink()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.printLL()
print(l1.FindLowest())  # Output: 10->20->30->40->50->None
print(l1.max_element())  # Output: 50


### Doubly Linked List Implementation in Python
class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def  __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyLinkedNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            return
        
    def printDLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_printDLL(self):
        current = self.head
        if current is None:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <- ")
            current = current.prev
        print("None")

dll = DoublyLinkedList()
dll.append(10)      
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.printDLL()  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> None
dll.reverse_printDLL()  # Output: 50 <- 40 <- 30 <-
