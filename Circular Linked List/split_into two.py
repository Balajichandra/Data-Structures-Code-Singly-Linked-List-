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
    def split(self,CLL1,CLL2):
        slow,fast = self.head,self.head
        while fast.next != self.head and fast.next.next != self.head:
            #slow_prv = slow
            slow = slow.next
            fast = fast.next.next    
        temp = slow
        new_head = slow.next
    
        CLL1.head = self.head    
        CLL1.last = slow
        CLL1.last.next = CLL1.head
        
        CLL2.head = new_head    
        CLL2.last = self.last
        CLL2.last.next = CLL2.head
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)
CLL = CircularLinkedList()
CLL1 = CircularLinkedList()
CLL2 =CircularLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    CLL.addend(node)
print("After adding data's...")
CLL.display()
print("Splitting into two linked list...")
CLL.split(CLL1,CLL2)
print("First part of linked list...")
CLL1.display()
print("Second part of linked list...") 
CLL2.display()   