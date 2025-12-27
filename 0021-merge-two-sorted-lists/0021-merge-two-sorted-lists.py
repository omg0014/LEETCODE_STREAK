# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        elif list1==None:
            return list2
        elif list2==None:
            return list1

        lst=[]
        curr=list1
        while curr:
            lst.append(curr.val)
            curr=curr.next

        curr=list2
        while curr:
            lst.append(curr.val)
            curr=curr.next
        lst.sort()
        new=ListNode(lst[0])
        curr=new
        for i in range(1,len(lst)):
            curr.next=ListNode(lst[i])
            curr=curr.next
        return new
        
        