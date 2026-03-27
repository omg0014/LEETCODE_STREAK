class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d={}
        first={}
        last={}
        for i in range(len(nums)):
            a=nums[i]
            if a in d:
                d[a]+=1
                last[a] = i
            else:
                d[a] = 1
                first[a] = i
                last[a] = i

        a=max(d.values())
        l=[]
        for i,j in d.items():
            if j==a:
                l.append(i)
        print(l)
        ans = float("inf")
        for i in l:
            ans = min(ans, last[i] - first[i]+1)
            # print(first[i],last[i])

        return ans

        