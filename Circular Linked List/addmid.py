class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedlist:
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
    def addmid(self,newNode):
        if self.head is not None:

            slow,fast = self.head,self.head
            while fast and fast.next != self.head:
                #slow_prv = slow
                slow = slow.next
                fast = fast.next.next
                print(slow.data,"\n",fast.data)
            temp = slow.next
            slow.next = newNode
            newNode.next = temp            
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)
CLL = CircularLinkedlist()
n = int(input("Enter the value of n in odd valus:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    CLL.addend(node)
print("After adding data's...")
CLL.display()
for i in range(1):
    data = int(input("Enter the middle value:"))
    node = Node(data)
    CLL.addmid(node)
print("After adding middle node...")
CLL.display()    