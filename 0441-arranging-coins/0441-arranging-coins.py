class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n==1:
        #     return 1
        a=1
        summ=0
        while summ+a<=n:
            summ+=a
            a+=1
        return a-1
        