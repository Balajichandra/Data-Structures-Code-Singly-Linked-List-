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
    def interchange_head_last(self):
        temp = self.head.data
        self.head.data = self.last.data
        self.last.data = temp
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
CLL.interchange_head_last()
print("After inter-changing data's...")
CLL.display()                 
