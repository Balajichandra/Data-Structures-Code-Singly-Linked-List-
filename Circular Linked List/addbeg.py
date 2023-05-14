class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addbeg(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            self.last.next = self.head
        else:
            newNode.next = self.head
            self.head = newNode
            #self.last = newNode
            self.last.next = self.head
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
    CLL.addbeg(node)
print("After adding data's...")
CLL.display()                