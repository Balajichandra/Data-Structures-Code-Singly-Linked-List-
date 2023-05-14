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
            self.head.prv = None 
        else:
            self.last.right = newNode
            newNode.left = self.last
            self.last = newNode
            self.last.right = None
    def delmid(self):
        if self.head is not None:
            slow,fast = self.head,self.head
            while fast and fast.right:
                slow = slow.right
                fast = fast.right.right
            temp = slow.data
            slow.left.right = slow.right
            slow.right.left = slow.left
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
print("After adding data's...")
DLL.display()
DLL.delmid()
print("After deleting middle node...")
DLL.display()                       