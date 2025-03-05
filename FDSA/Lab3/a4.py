class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def append_node(head,data):
    newnode=Node(data)
    
    if head is None:
        return newnode
    curr=head#n1
    while curr.next is not None:#n2 #n3
        curr=curr.next
    curr.next=newnode
    return head

def searchnode(head,key):
    curr=head
    r=False
    if head is None:
        return None
    while curr is not None:
        if curr.data==key:
            r=True
            break
        curr=curr.next
    return r

def displaylist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next
    print()

n1=Node(1)
n2=Node(2)
n3=Node(3)

n1.next=n2
n2.next=n3

head=n1
print("Before appending: ")
displaylist(head)
print("After appending: ")
append_node(n1,4)
displaylist(head)

print()
ex=searchnode(head,5)
if ex==True:
    print("exists")
else:
    print("does not exist")

print("\nThe linked list is : ")
displaylist(head)