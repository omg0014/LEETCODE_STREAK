class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        c=0
        for i in batteryPercentages:
            a=i-c
            if a<0:
                a=0
            if a>0:
                c+=1
        return c

        