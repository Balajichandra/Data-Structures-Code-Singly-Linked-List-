from typing import NewType


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
    def move_last_front(self):
        current = self.head
        while current.next != self.last:
            current = current.next
        self.last.next = self.head
        self.head = self.last
        self.last = current
        self.last.next = None
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()    
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL.move_last_front()                        
print("After moving last to front...")
SLL.display()