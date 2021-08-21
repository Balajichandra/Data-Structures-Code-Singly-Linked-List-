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
    def rem_dup(self):
        current = self.head
        while current != None and current.next != None:
            current2 = current
            while current2.next != None:
                if current.data == current2.next.data:
                    dup = current2.next
                    current2.next = current2.next.next
                    del(dup)
                else:
                    current2 = current2.next
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
SLL.rem_dup()
print("After removing duplicates...")
SLL.display()                                  
                    