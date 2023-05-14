class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            self.head.left = None
        else:
            self.last.right = newNode
            newNode.left = self.last
            self.last = newNode
            self.last.right = None
    def delend(self):
        if self.head is not None:
            temp = self.last
            self.last = self.last.left
            self.last.right = None
            del(temp)
        else:
            print("Sorry no node to delete...")
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.right
DLL = DoublyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    DLL.addend(node)
print("After adding data's into linked list...")
DLL.display()
DLL.delend()
print("After deleting last node...")
DLL.display()                            