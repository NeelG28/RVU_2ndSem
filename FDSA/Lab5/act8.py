class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circular:
    def __init__(self):
        self.head=None
        self.next=None

    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            newnode.next=self.head
            current.next=newnode

    
    def delbeg(self):
        temp=self.head
        current=self.head
        while current.next!=self.head:
            current=current.next
        current.next=temp.next
        self.head=temp.next
        del temp

    def delend(self):
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        temp=current.next
        current.next=self.head
        del temp

    def delnode(self,key):
        if self.head is None:
            print("CLL is empty")
            return
        
        if self.head.data==key:
            if self.head.next==self.head:
                self.head=None
                return
            current=self.head
            while current.next!=self.head:
                current=current.next
            temp=self.head
            current.next=self.head.next
            self.head=self.head.next
            del temp
            return
        
        current=self.head
        while current.next!=self.head and current.next.data!=key:
            current=current.next

        if current.next==self.head:
            print("Given key is not present")
            return
        
        temp=current.next
        current.next=current.next.next
        del temp

    def traverse(self):
        current=self.head
        while True:
            print(current.data,end=" " if current.next!=self.head else "")
            current=current.next
            if current==self.head:
                break
        print()

cll=circular()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_end(40)
cll.traverse()
cll.delbeg()
cll.traverse()
cll.delend()
cll.traverse()
cll.delnode(20)
cll.traverse()