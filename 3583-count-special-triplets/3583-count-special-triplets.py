class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD=10**9+7
        from collections import Counter
        right=Counter(nums)
        left=Counter()
        ans=0
        j=0
        n=len(nums)
        while j<n:
            x=nums[j]
            right[x]-=1
            need=x*2
            ans=(ans+left[need]*right[need])%MOD
            left[x]+=1
            j+=1
        return ans
        