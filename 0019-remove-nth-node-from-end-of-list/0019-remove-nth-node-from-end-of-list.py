# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        curr=head
        while curr!=None:
            curr=curr.next
            c+=1
        if n == c:
            return head.next
        if head==None:
            return None
        curr=head
        for i in range(c-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return head

        