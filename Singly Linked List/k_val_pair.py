##WAP to find count pairs from two linked list whoose sum is equal to k...
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
    def find_k_ntimes(self,key):
        val_1,val_2 = 0,0
        current = self.head
        flag = False
        while current != None and current.next != None:
            current2 = current
            while current2.next != None:
                if key ==(current.data+current2.next.data):
                    flag = True
                    val_1 = current.data
                    val_2 = current2.next.data
                    break
                else:
                    current2 = current2.next
                    flag = False
            current = current.next
        if flag == True:
            print("Given k matches pair values:",val_1,val_2)
        else:
            print("Sorry no key is found...")                    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
SLL = SinglyLinkedList()
n = int(input("ENter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
key = int(input("Enter the key to be found n times:"))
SLL.find_k_ntimes(key)                                                       