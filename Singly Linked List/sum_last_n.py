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
    def last_sum_k(self,k,n):
        current = self.head
        cnt = n - k
        while cnt:
            current = current.next
            cnt-=1
        tot = 0
        while current:
            tot = tot + current.data
            current = current.next
        print("Sum of last K nodes:",tot)    
    def display(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()
SLL = SinglyLinkedList()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
K = int(input("Enter the value of k:"))
SLL.last_sum_k(K,n)                                  
