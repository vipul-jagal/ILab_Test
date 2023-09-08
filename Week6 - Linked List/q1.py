# Reverse a doubly linked list


def reverse(llist):
    if llist is None:
        return llist
    if llist.prev is None and llist.next is None:
        return llist
    curr=llist
    while curr.next is not None:
        curr.prev,curr.next=curr.next,curr.prev
        curr=curr.prev
    curr.prev,curr.next=curr.next,curr.prev
    return curr
