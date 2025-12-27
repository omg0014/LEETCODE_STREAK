# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        lst=[]
        while curr:
            lst.append(curr.val)
            curr=curr.next
        n=len(lst)
        k = k % n 
        arr=lst[n-k:n]+lst[:n-k]
        new=ListNode(arr[0])
        curr=new
        for i in range(1,len(arr)):
            curr.next=ListNode(arr[i])
            curr=curr.next
        return new
        