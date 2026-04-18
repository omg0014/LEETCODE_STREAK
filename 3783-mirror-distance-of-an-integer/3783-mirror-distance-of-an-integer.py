class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=str(n)
        a=int(s[::-1])
        return abs(n-a)
        