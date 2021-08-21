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
    def del_without_head(self,node_ptr):
        temp = node_ptr.next
        node_ptr.data = temp.data
        node_ptr.next = temp.next
        del(temp)
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
    data = input()
    node = Node(data)
    SLL.addend(node)
print("After adding data's...")
SLL.display()
SLL.del_without_head(SLL.head.next)        
print("After deleting node...")    
SLL.display()