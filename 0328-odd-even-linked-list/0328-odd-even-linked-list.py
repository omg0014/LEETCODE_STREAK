# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        odd=[]
        even=[]
        c=0
        if head==None:
            return None
        while curr:
            if c%2==0:
                even.append(curr.val)
            else:
                odd.append(curr.val)
            curr=curr.next
            c+=1
        arr=even+odd
        first=ListNode(arr[0])
        curr=first 
        for i in range(1,c):
            curr.next=ListNode(arr[i])
            curr=curr.next
        return first
        