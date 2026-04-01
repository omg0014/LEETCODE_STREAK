class Solution:
    def minimumSum(self, num: int) -> int:
        s=str(num)
        l=[]
        for i in s:
            l.append((i))
        l.sort()
        a=(l[0]+l[3])
        b=l[1]+l[2]
        # print(l)
        # print (a)
        return (int(a)+int(b))
        

        