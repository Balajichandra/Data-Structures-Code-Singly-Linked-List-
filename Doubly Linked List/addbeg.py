class Node:
    def __init__(self,data):
        self.data = data
        self.prv = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def addbeg(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prv = newNode
            self.head = newNode
            self.head.prv = None 
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
DLL = DoublyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the data's into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    DLL.addbeg(node)
print("After adding  data's")
DLL.display()                                       