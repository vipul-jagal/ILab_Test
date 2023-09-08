# Find Merge Point of Two Lists

def lenOfLL(head):
    l=0
    while head is not None:
        l+=1
        head=head.next
    return l
def findMergeNode(head1, head2):
    n1=lenOfLL(head1);
    n2=lenOfLL(head2);
    k=abs(n1-n2);
    if(n1>n2):
        while(k!=0):
            head1=head1.next
            k-=1
    else:
        while(k!=0):
            head2=head2.next
            k-=1
    while(head1!=head2):
        head1=head1.next
        head2=head2.next
    return head1.data
