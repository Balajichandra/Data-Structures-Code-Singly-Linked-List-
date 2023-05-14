class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            self.last.next = self.head
        else:
            self.last.next = newNode
            self.last = newNode
            self.last.next = self.head
    def circular_check(self):
        if self.last.next != None:
            print("The given linked list is circular...")
        else:
            print("Sorry the linked list do not form circular...")
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)
CLL = CircularLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input()) 
    node = Node(data)
    CLL.addend(node)
print("After adding data's...")
CLL.display()
CLL.circular_check()                       
