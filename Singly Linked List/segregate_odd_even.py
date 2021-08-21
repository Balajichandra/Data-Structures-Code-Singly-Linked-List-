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
    def segregate(self):
        if self.head is None:
            print("Sorry linked list is empty...")
            return
        else:
            current = self.head
            while current.next != None:
                if (current.data % 2 == 0 and current.next.data % 2 != 0):
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                    current = current.next
                    print("IF PART",current.data," ",current.next.data)
                    
                else:
                    current = current.next
                    print("ELSE PART",current.data,end=' ')
                    
    def display(self):
        current = self.head
        while current != None:
            print(current.data,end=' ')
            current = current.next
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:")) 
print("Enter the value into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL.segregate()
print("After seprating odd and even elements to each end...")               
SLL.display()