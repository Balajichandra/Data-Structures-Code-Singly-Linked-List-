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
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()    
    def Intersect(self,SLL2):
        common = []
        current1 = self.head
        current2 = SLL2.head
        flag = True
        while current1 != None and current2 != None:
            if current1.data != current2.data:
                flag = False           
            current1 = current1.next
            current2 = current2.next
        if flag == True:
            print("The given linked list are identical...")  
        else:
            print("The given list are not identical...")                 
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list 1...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("The elements of Singly Linked List 1...")
SLL.display()    
SLL2 = SinglyLinkedList()
m = int(input("Enter the value of m:"))
print("Enter the values for Singly Linked List 2...")
for j in range(m):
    data = int(input())
    node = Node(data)
    SLL2.addend(node)
print("After adding data's...")
SLL2.display() 
SLL.Intersect(SLL2)   
