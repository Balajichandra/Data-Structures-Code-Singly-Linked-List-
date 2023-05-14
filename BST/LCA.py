class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key 
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root
def inorder(root):
    if root :
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def PCA(root,l1,l2):
    if root is None:
        print("BST is empty...")
        return
    if (root.val > l1 and root.val> l2):
        return PCA(root.left,l1,l2)
    if (root.val < l1 and root.val < l2):
        return PCA(root.right,l1,l2)
    return root        
r = Node(20)
r = insert(r,8)
r = insert(r,22)
r = insert(r,4)
r = insert(r,12)
r = insert(r,10)
r = insert(r,14)
print("Inorder traversal...")
inorder(r)                                        
n1 = 10
n2 = 14
t = PCA(r,n1,n2)
print(n1,n2,t.val)























