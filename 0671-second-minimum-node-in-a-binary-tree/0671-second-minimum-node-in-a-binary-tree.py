# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        lst=[]
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
        inorder(root)
        l=(list(set(lst)))
        l.sort()
        if len(l)==0 or len(l)==1:
            return -1
        else:
            return l[1]
        