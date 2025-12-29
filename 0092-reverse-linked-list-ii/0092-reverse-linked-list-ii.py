# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        lst=[]
        while curr:
            lst.append(curr.val)
            curr=curr.next
        arr=lst[:left-1]+lst[left-1:right][::-1]+lst[right:]
        first=ListNode(arr[0])
        curr=first
        for i in range(1,len(arr)):
            curr.next=ListNode(arr[i])
            curr=curr.next
        return (first)
