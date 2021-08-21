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
    def intersect(self,SLL2):
        common = []
        current1 = self.head
        while current1 != None and current1.next != None:
            current2 = SLL2.head
            #print(current2.data,end=' ')
            while current2.next != None:
                if current1.data == current2.next.data:
                    #SLL3.addend(Node(current1.data))
                    print("Intersection elements:",current1.data,end='') 
                    current2 = current2.next
                    break
                else:
                    current2 = current2.next
            current1 = current1.next
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
print("After adding data's...")
SLL.display()
SLL2 = SinglyLinkedList()
m = int(input("ENter the value of m:"))
print("Enterr the values into linked list 2") 
for j in range(m):
    data = int(input())
    node = Node(data)
    SLL2.addend(node)
print("After adding data's...")
SLL2.display()
SLL3 = SinglyLinkedList()
SLL.intersect(SLL2)
SLL3.display()    
