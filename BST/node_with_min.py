class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
def find_min(root):
    if root:
        return find_min(root.left)
    
r = Node(50)
r = insert(r,20)
r = insert(r,40) 
r = insert(r,70)
r = insert(r,80)
r = insert(r,60)
r = insert(r,30)
inorder(r)
res = find_min(r)               
    