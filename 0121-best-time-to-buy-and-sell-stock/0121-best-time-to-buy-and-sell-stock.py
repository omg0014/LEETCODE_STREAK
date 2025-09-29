class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float("inf")
        max_profit=0
        for i in prices:
            minn=min(i,minn)
            max_profit=max(i-minn,max_profit)
        return max_profit
        