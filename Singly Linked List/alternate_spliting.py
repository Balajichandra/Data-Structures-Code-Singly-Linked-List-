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
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()    
    def AlternateSpliting(self):
        current = self.head
        while current:
            SLL_dup1.addend(Node(current.data))
            current = current.next
            SLL_dup2.addend(Node(current.data))
            current = current.next
            
SLL = SinglyLinkedList()    
SLL_dup1 = SinglyLinkedList()
SLL_dup2 = SinglyLinkedList()  
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):                              
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's")
SLL.display()    
SLL.AlternateSpliting()
print("After splitting data's ---> First Linked List...")
SLL_dup1.display()
print("Second Linked List")
SLL_dup2.display()