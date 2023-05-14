class Node:
    def __init__(self,data):
        self.data = data
        self.prv = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            #self.head.prv = None
        else:                 
            self.last.next = newNode
            newNode.prv = self.last 
            self.last = newNode
    def reverse(self):
        temp = None
        current = self.head        
        while current is not None:
            temp = current.prv
            current.prv = current.next
            current.next = temp
            current = current.prv
        if temp is not None:
            self.head = temp.prv 
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
DLL = DoublyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    DLL.addend(node)
print("After adding nodes...")
DLL.display
DLL.reverse()
print("After reversing...")
DLL.display()                      
