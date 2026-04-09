import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=0
        odd=0
        for i in range(2,(2*n)+1,2):
            print(i)
            even+=i
        for i in range(1,(2*n)+1,2):
            odd+=i
        return math.gcd(even,odd)
        