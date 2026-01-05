# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        curr=head
        while curr:
            lst.append(curr.val)
            curr=curr.next
        lst.sort()
        if len(lst)==0:
            return None
        a=ListNode(lst[0])
        start = a
        for i in range(1,len(lst)):
            start.next=ListNode(lst[i])
            start=start.next
        return a
        
        