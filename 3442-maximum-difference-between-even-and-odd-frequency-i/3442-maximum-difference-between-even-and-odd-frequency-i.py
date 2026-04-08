class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        even=[]
        odd=[]
        for i in d.values():
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd.sort()
        # print(even,odd)
        return max(odd[-1]-even[0],odd[0]-even[-1])

        