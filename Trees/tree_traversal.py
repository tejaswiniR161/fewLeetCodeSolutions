root=None
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def show(self):
        return self.data

options={1:add,2:inorder}

def add():
    data=input("Enter the node value (int)")
    newnode=node(int(data))
    if(root==None):
        root=newnode
    else:
        insert(newnode,root)

def insert(newnode,nextroot):
    for()

try:
    ip=input("Enter your choice\n 1:add new node\n 2:inorder\n")
    options[int(ip)]()

except except KeyboardInterrupt:
    print("Closing..")