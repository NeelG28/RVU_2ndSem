class Doubly:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def delete_node(self,key):
        if self.head is None:
            print("list empty")                                                                                                                                                          
            return
        
        temp = self.head
        while temp is not None and temp.data != key:
            temp = temp.next
        
        if temp is None:
            print(f"Key {key} not found in the list.")
            return
        
        if temp == self.head and temp.next is None:  # Only one node in list
            self.head = None
        elif temp == self.head:  # Deleting head
            self.head = temp.next
            self.head.prev = None
        elif temp.next is None:  # Deleting tail
            temp.prev.next = None
        else:  # Deleting middle node
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        
        del temp

    def travback(self):
        back=self.tail
        while back is not None:
            print(back.data,end=" ")
            back=back.prev
        print()
    
    def displaylist(self):

        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

n1 = Doubly(1)
n2 = Doubly(2)
n1.next=n2
n2.prev=n1
n3 = Doubly(4)
n2.next=n3
n3.prev=n2
n4 = Doubly(7)
n3.next=n4
n4.prev=n3

dll_wrk = dll()
dll_wrk.head = n1
dll_wrk.tail=n4

# Display initial list
print("Initial list:")
dll_wrk.displaylist()
print("List after deletion:")
dll_wrk.delete_node(2)
dll_wrk.displaylist()

print("List in reverse : ")
dll_wrk.travback()
