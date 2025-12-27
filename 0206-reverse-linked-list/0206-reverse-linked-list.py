# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        lst=[]
        while curr:
            lst.append(curr.val)
            curr=curr.next
        lst=lst[::-1]
        new=ListNode(lst[0])
        curr=new
        for i in range(1,len(lst)):
            curr.next=ListNode(lst[i])
            curr=curr.next
        return new
        
        