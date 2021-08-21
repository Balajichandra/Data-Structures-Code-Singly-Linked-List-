class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
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
    def find(self,k,n):
        current = self.head
        cnt =  n - k + 1
        cnt-=1
        while cnt:
            current = current.next
            cnt-=1
        print(current.data)
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
SLL = SingleLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
pos = int(input("Enter the n from last:")) 
SLL.find(pos,n)                       
