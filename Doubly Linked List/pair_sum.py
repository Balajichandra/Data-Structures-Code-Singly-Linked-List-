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
            newNode.prv = self.last
            self.last = newNode
    def pair_sum(self,k):
        current = self.head
        while current != None and current.next != None:
            current2 = current
            while current2.next != None:
                if ((current2.next.data + current.data) == k):
                    print("Pair data's:",current.data,current2.next.data)
                    current2 = current2.next
                else:
                    current2 = current2.next
            current = current.next 
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
print("After adding nodes...")
DLL.display()
K = int(input("Enter the value of k:"))
DLL.pair_sum(K)
