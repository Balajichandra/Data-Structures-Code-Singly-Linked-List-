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
    def multiply(self,SLL2):
        current1 = self.head
        current2 = SLL2.head
        num1 = 0
        num2 = 0
        while current1 != None or current2 != None:
            if current1 != None:
                num1 = num1 * 10 + current1.data
                current1 = current1.next
            if current2 != None:  
                num2 = num2 * 10 + current2.data
                current2 = current2.next
        print("Multiplication of two linked list:",num1*num2)
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()    
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input()) 
    node = Node(data)
    SLL.addend(node)
print("Elements of first linked list...")
SLL.display()    
SLL2 = SinglyLinkedList()
m = int(input("Enter the value of m:"))
print("Enter the values of second linked list...")
for j in range(m):
    data_1 = int(input())
    node_1 = Node(data_1)
    SLL2.addend(node_1)
print("Elements of second linked list...")
SLL2.display()
SLL.multiply(SLL2)