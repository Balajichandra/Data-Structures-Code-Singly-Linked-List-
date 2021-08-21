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
    def rotate(self,k):
        cnt = k
        current = self.head
        temp = self.head
        while cnt:
            current = current.next
            cnt-=1
        #print(current.data)
        self.last.next = self.head
        self.head = current.next
        self.last = current
        self.last.next =None
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
K = int(input("Enter number of times rotation have to be done:"))
SLL.rotate(K)                        
print("After rotating K times...")
SLL.display()