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
    def strcmp(self,SLL1):
        a = self.head
        b = SLL1.head
        while a != None and b != None:
            if a.data == b.data:
                a = a.next
                b = b.next
                flag = True
            else:
                flag = False
                break    
        if flag == True:
            print("Both strings are equal...")
        else:
            print("Both strings are not equal...")
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()

SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = input()
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL1 = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = input()
    node = Node(data)
    SLL1.addend(node)
print("After adding data's...")
SLL1.display() 
SLL.strcmp(SLL1)                           
                