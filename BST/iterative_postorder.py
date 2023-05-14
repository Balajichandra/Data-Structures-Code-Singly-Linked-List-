class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        else:
            current = self.root
            while True:
                parent = current
                if data < current.data:
                    current = current.left
                    if current == None:
                        parent.left = newNode
                        return               
                else:
                    current = current.right
                    if current == None:
                        parent.right = newNode
                        return
    def postorder(self,node):
        if self.root is None:
            print("Sorry no BST...")
        else:
            if node.left != None:
                self.postorder(node.left)
            if node.right != None:
                self.postorder(node.right)
            print(node.data,end=' ')
BST = BinarySearchTree()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    BST.insert(data)
print("After adding data's...")
BST.postorder(BST.root)                                                         