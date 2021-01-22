from Node import *

n1=Node(1)
n2=Node(2)
n3=Node(3)
n1.next=n2
n2.next=n3
head=n1
ptr=head
while ptr:
    print(ptr.data)
    ptr=ptr.next
