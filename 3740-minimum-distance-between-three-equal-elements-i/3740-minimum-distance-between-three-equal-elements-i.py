class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        for i  in range (len(nums)):
            a=nums[i]
            if a in d:
                d[a].append(i)
            else:
                d[a]=[i]
        lst=[]
        for i,j in d.items():
            if len(j)>=3:
                for m in range(2,len(j)):
                    x=j[m-2]
                    y=j[m-1]
                    z=j[m]
                    new=abs(x-y)+abs(y-z)+abs(x-z)
                    lst.append(new)
        if len(lst)==0:
            return -1
        return min(lst)



        