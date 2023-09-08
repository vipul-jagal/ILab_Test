# Insert a node into a double linked list


def sortedInsert(llist, data):
    newNode=DoublyLinkedListNode(data)
    tail=llist
    #insertion before head
    if newNode.data<llist.data:
        newNode.next=tail
        tail.prev=newNode
        llist=newNode
        return llist
    #insertion in between
    while tail.next is not None:
        if tail.next.data<data:
            tail=tail.next
        else:
            newNode.next=tail.next
            newNode.prev=tail
            tail.next=newNode
            return llist
    #insertion after tail
    newNode.prev=tail
    tail.next=newNode
    return llist
