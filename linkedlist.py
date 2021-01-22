from Node import *

def sizeofLL(head):
    size=0
    while(head!=None):
        size+=1
        head=head.next


    return size

def printLinkedList(head):
    while(head!=None):
        print(head.data)
        head=head.next

def printLinkedList_rec(head):
    if(head!=None):
        if (head.next!=None):
            printLinkedList_rec(head.next)
        print(head.data)

def delete(head,val):
    orighead=head
    if head==None:
        return
    if orighead.data==val:
        return orighead.next
    while(head!=None and head.next!=None):
        if head.next.data==val:
            head.next=head.next.next
            return orighead

        head=head.next

def deleteDups(head):

    while(head!=None and head.next!=None):
        while (head.next.data==head.data):
            head.next=head.next.next

        head=head.next



        head=head.next

n1=Node(1)
n2=Node(3)
n3=Node(3)
n4=Node(3)
n5=Node(4)
n6=Node(5)
n7=Node(6)
n8=Node(6)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8


head=n1
delete(head,5)
#printLinkedList_rec(head)
printLinkedList(head)
print(sizeofLL(head))
