class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        arr=[]
        for i in s:
            a=int(i)
            arr.append(a)
        arr.sort(reverse=True)
        return arr[0]*arr[1]

        