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
    def delmid(self):
        if self.head is not None:
            slow,fast = self.head,self.head
            slow_prv = self.head
            while fast and fast.next:                        
                slow_prv = slow
                slow = slow.next
                fast = fast.next.next
            temp = slow.data
            slow_prv.next = slow.next
            del(temp)    
            #print(slow.data)
            #print(slow_prv.data)
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into list")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding all nodes...")
SLL.display()            
SLL.delmid()
print("After deleting mid node...")
SLL.display() 