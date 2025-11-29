class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        c=0
        a=3
        if n==1:
            return True
        while a**c<=n:
            if a**c==n:
                return True
            c+=1
        return False
        