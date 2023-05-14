class Node:
    def __init__(self,data):
        self.data = data
        self.prv = None
        self.next = None
class DoublyLinkedList:
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
        if self.head is not None:
            slow,fast = self.head,self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            temp = slow.next
            temp.prv = slow  
            #print(slow.prv)  
            slow.next = newNode
            newNode.prv = slow
            newNode.next = temp
            temp.prv = newNode
            #slow.prv.next = newNode
            #newNode.prv = slow.prv.next
            #newNode.next = slow
            #slow.prv = newNode                          
            #slow.next.prv = slow.prv 
            #del(temp)
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
DLL = DoublyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    DLL.addend(node)
print("After adding data's...") 
DLL.display()
print("Enter the middle value into linked list...")
for i in range(1):                       
    data = int(input())
    node = Node(data)
    DLL.addmid(node)
print("After adding middle node...")
DLL.display()    