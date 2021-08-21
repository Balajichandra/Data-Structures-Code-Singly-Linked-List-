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
    def make_mid_head(self):
        slow_prv,slow,fast = self.head,self.head,self.head
        while fast and fast.next != None:
            slow_prv = slow
            slow = slow.next
            fast = fast.next.next
        self.last.next = self.head
        self.head = slow    
        self.last = slow_prv
        self.last.next = None
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
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL.make_mid_head()
print("After making mid as head...")
SLL.display()    

