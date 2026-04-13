class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        current=0
        while k>0:
            if numOnes>0:
                current+=1
                numOnes-=1
                k-=1
            elif numZeros>0:
                numZeros-=1
                k-=1
            elif numNegOnes>0:
                current-=1
                numNegOnes-=1
                k-=1
        return current



        