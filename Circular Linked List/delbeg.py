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
    def delbeg(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            self.last.next = self.head
            del(temp)
        else:
            print("Sorry no node to delete...")                            
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:        
            current = current.next
            print(current.data)
CLL = CircularLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list") 
for i in range(n):
    data = int(input())
    node = Node(data) 
    CLL.addend(node)
print("After adding all nodes...")  
CLL.display()
CLL.delbeg()
print("After deleting head node...")
CLL.display()            