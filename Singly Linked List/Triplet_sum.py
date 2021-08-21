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
    def triplet(self,SLL1,SLL2,k):
        flag = False
        a = self.head
        sum = 0
        while a != None:
            b = SLL1.head
            c = SLL2.head
            while (b != None and c != None):
                sum = a.data+b.data+c.data
                if sum == k:
                    flag = True
                    print("Triplet found:",a.data,",",b.data,",",c.data)
                    break
                elif sum < k:
                    b = b.next
                else:
                    c = c.next
            a = a.next
        if flag == False:
            print("Sorry no triplet found")
        else:
            pass    
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL2 = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL2.addend(node)
print("After adding data's...")
SLL2.display()
SLL1 = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("ENter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL1.addend(node)
print("After adding data's...")
SLL1.display()
k = int(input("Enter the K value:"))                        
SLL.triplet(SLL1,SLL2,k)