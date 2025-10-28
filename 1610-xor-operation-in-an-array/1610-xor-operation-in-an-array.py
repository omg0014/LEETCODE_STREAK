class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c=0
        for i in range(n):
            x=(start+(2*i))
            c^=x
        return c
        
        