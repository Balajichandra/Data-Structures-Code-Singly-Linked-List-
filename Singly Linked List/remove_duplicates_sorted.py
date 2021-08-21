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
    def remove_dup(self):
        current = self.head
        print(current.next.data)
        print(current.data)
        while current.next != None:
            if current.data == current.next.data:
                new = current.data 
                temp = current.next.next
                current.next = None
                current.next = temp
                del(new)
            else:
                current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the vlaues into linked list")
for i in range(n):
    data = int(input()) 
    node = Node(data)
    SLL.addend(node)
print("After adding data's")
SLL.display()
SLL.remove_dup()
print("After removing duplicates...")
SLL.display()                                                   