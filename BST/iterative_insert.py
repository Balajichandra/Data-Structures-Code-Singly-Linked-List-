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
    def inorderTraversal(self, node):  
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return;  
        else:  
            if(node.left != None):  
                self.inorderTraversal(node.left);  
            print(node.data, end=" ");  
            if(node.right != None):  
                self.inorderTraversal(node.right);  
"""                
BST = BinarySearchTree()
BST.insert(50)
BST.insert(70)
BST.insert(60)
BST.insert(40)
BST.insert(20)
BST.insert(80)
BST.insert(30)
print("After inserting data's...")
BST.inorderTraversal(BST.root)            
"""
BST = BinarySearchTree()
n = int(input("Enter the value of n:"))
print("Enter the values into linked list...")
for i in range(n):
    data = int(input())
    BST.insert(data)
print("After adding data's...")
BST.inorderTraversal(BST.root)    