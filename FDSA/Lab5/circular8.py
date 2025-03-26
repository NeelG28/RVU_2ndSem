class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circular:
    def __init__(self):
        self.head=None
        self.next=None

    def insertbeg(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            
            newnode.next=self.head
            current.next=newnode
            self.head=newnode
        
    

    def traverse(self):
            if self.head is None:
                 print("CLL is empty")
                 return
            current=self.head
            
            while True:
                print(current.data,end=" ")
                current=current.next
                if current==self.head:
                    break
            print()

cll=circular()
cll.insertbeg(10)
cll.insertbeg(20)
cll.insertbeg(30)

cll.traverse()
