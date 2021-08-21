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
            self.last.next = None        
    def addmid(self,newNode):
        if self.head is None:
            SLL.addend(self,newNode) 
        else:
            slow,fast = self.head,self.head
            slow_bef = self.head
            while fast and fast.next:
                slow_bef = slow
                slow = slow.next
                fast = fast.next.next    
            temp = slow_bef.next
            slow_bef.next = newNode
            newNode.next = temp
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()    
SLL =SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's")
SLL.display()                                       
print("Enter the middle node value:")
for i in range(1):
    data = int(input())
    node = Node(data)
    SLL.addmid(node)
print("After adding middle node...")
SLL.display()    