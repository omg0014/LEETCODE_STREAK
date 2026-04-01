class Solution:
    import math
    def isThree(self, n: int) -> bool:
        a=math.sqrt(n)
        b=int(math.sqrt(n))
        if a-b!=0:
            return False
        arr=[0 for _ in range(b+1)]
        arr[0]=arr[1]=1
        for i in range(2,b+1):
            for j in range(i*i,b+1,i):
                arr[j]=1
        if arr[b]==0:
            return True
        return False
            
        