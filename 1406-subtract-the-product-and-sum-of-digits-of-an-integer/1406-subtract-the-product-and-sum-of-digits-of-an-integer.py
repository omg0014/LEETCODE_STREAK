class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        summ=0
        m=1
        for i in s:
            m*=int(i)
            summ+=int(i)
        return m-summ

        