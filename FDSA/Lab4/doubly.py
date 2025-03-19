class Doubly:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertbeg(head, data):
    newnode = Doubly(data)
    if head is None:
        head = newnode
    else:
        newnode.next = head
        head.prev = newnode
        head = newnode
    
    return head

def insertend(tail, data):
    newnode = Doubly(data)
    if tail is None:
        tail = newnode
    else:
        newnode.prev = tail 
        tail.next = newnode
        tail = newnode
    
    return tail

def displaylist(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

# Initial nodes
n1 = Doubly(1)
n2 = Doubly(2)
n1.next=n2
n2.prev=n1
n3 = Doubly(4)
n2.next=n3
n3.prev=n2
head = n1
tail = n3

# Display initial list
print("Initial list:")
displaylist(head)

# Insert at the beginning
head = insertbeg(head, 0)
print("After inserting 0 at the beginning:")
displaylist(head)

# Insert at the end
tail = insertend(tail, 5)
print("After inserting 5 at the end:")
displaylist(head)
