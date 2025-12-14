# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst=[]
        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
        inorder(root)
        arr=[]
        for i in lst:
            arr.append(i)
        arr.sort()
        d={}
        for i in arr:
            if i in d:
                return False
            else:
                d[i]=1
        if arr==lst:
            return True
        else:
            return False
        