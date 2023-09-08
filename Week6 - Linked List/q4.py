# Get Node Value

def getNode(llist, positionFromTail):
    #initialize slow and fast as llist
    slow=llist
    fast=llist
    k=positionFromTail
    while fast is not None and k!=0:
        fast=fast.next
        k-=1
    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    return slow.data
