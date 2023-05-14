class Node:
    def __init__(self,data):
        self.data = data
        self.prv = None
        self.nxt = None 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            self.head.prv = None
        else:
            self.last.nxt = newNode
            newNode.prv = self.last
            self.last = newNode
            self.last.nxt = None
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.nxt
        print()
DLL = DoublyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list")
for i in range(n):
    data = int(input())
    node = Node(data)
    DLL.addend(node)
print("After adding all nodes...")
DLL.display()                                        