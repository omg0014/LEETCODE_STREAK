class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            a=nums[i]
            if a in d:
                d[a].append(i)
            else:
                d[a]=[i]
        for i,j  in d.items():
            if len(j)>1:
                for x in range(1,len(j)):
                    if abs(j[x-1]-j[x])<=k:
                        return True
        return False

        