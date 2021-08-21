class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def addbeg(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
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
    SLL.addbeg(node)
print("After adding all nodes...")
SLL.display()                                       