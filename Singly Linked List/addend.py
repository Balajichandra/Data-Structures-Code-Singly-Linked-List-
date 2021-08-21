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
            self.last.next = None
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next                        
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:")) 
print("Enter the values into linked list...")
for i in range(n):
    data = int(input()) 
    node = Node(data) 
    SLL.addend(node)
print("After adding all values in linked list...")
SLL.display()             