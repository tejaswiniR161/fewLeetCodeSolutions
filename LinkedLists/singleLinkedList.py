#SingleLinkedList basics

class node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def show(self):
        return self.value

def add_node_end():
    global head,prev
    value=input("Enter new node value: ")
    newnode=node(value)
    print("new node address ",newnode)
    print("id from the id() : ",id(newnode))
    if head==None:
        head=newnode
    else:
        p=head
        while p.next is not None:
            p=p.next
        p.next=newnode
        
def display_all_nodes():
    global head
    global prev
    if head is None:
        print("LL is empty")
    else:
        p=head
        while p is not None:
            print("Value = "+p.show())
            p=p.next   

def delete_node_end():
    global head
    p=head
    prev=p
    if head is None:
        print("No elements to delete")
    else:
        while p.next is not None:
            prev=p
            p=p.next
        prev.next=None
        del p     
    print("in the delete_node_end function")

def reverse_all_nodes():
    global head
    if head is None:
        print("List is empty!")
    elif head.next is None:
        print("Has just one element! So, Reversed! HAve fun!")
    else:
        c=head.next
        p=head
        n=head
        p.next=None
        while c is not None:
            n=c.next
            print("p value is ",p.show())
            c.next=p
            p=c
            c=n
        print("p is currently at ", p.show())
        head=p
        print("head is at ",head.show())

options={1:add_node_end,2:delete_node_end,3:display_all_nodes,4:reverse_all_nodes}
head=None
prev=None
try:
    while True:
        choice=input("Enter your choice \n 1:Add new node in the End\n 2:Delete a node from the end\n 3:Diplay all the nodes\n 4:Reverse all the nodes\n")

        options[int(choice)]()
        
except KeyboardInterrupt:
    print("Closing!")