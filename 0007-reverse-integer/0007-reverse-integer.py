class Solution:
    def reverse(self, x: int) -> int:
        s1=str(x)
        b=True
        if s1[0]=="-":
            b=False
        x=abs(x)
        s=str(x)
        a=s[::-1]
        rev = int(a)
        if not b:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev
        

        