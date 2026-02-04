class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s=sum(nums)
        avg=s//len(nums)
        nums.append(avg)
        nums.sort()
        c=0
        a=0
        if avg < 0:
            avg=1
            
        for i in nums:
            if i<avg:
                c+=1
            elif i==avg :
                avg+=1

            elif avg!=i and avg>0:
                return avg
        return avg



        