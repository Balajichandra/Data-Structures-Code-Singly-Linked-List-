class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def addend(self,newNode):
        if self.head is None:
            self.head = newNode
            self.last = newNode
            self.last.next = self.head
        else:
            self.last.next = newNode
            self.last = newNode
            self.last.next = self.head
    def delmid(self):
        if self.head is not None:
            slow_prv,slow,fast = self.head,self.head,self.head
            while fast and fast.next != self.head:
                slow_prv = slow
                slow = slow.next
                fast = fast.next.next
            temp = slow
            slow_prv.next = slow.next
            del(temp)
        else:
            print("Sorry no node to delete")
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)
CLL = CircularLinkedList() 
n = int(input("Enter the value of n in odd:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input()) 
    node = Node(data)
    CLL.addend(node)
print("After adding data's...")
CLL.display()
CLL.delmid()
print("After deleting middle node...")
CLL.display()