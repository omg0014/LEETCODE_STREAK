class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s=str(num)
        l=list(s)
        if num==0:
            return True
        if l[-1]=="0":
            return False
        else:
            return True
        