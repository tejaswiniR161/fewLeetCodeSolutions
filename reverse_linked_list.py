#accpeted code for ll reversal

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            print("List is empty!")
        elif head.next is None:
            print("Has just one element! So, Reversed! Have fun!")
        else:
            c=head.next
            p=head
            n=head
            p.next=None
            while c is not None:
                n=c.next
                #print("p value is ",p.show())
                c.next=p
                p=c
                c=n
                #print("p is currently at ", p.show())
            head=p
            #print("head is at ",head.show())
        return head