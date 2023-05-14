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
    def find(self,val):
        if self.head is not None:
            current = self.head
            while  current.next != self.head:
                if current.data == val:
                    flag = True
                    break 
                else:
                    current = current.next
                    flag = False                      
            if flag == True:
                print("The given node is present...")
            else:
                print("Sorry no node is present")    
    def display(self):
        current = self.head
        print(current.data)
        while current.next != self.head:
            current = current.next
            print(current.data)
CLL = CircularLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    CLL.addend(node)
print("After adding data's...")
CLL.display()
val = int(input("Enter the value to be found:"))
CLL.find(val)                                