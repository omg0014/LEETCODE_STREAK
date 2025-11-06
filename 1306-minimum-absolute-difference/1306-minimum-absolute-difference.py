class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn=float("inf")
        l=0
        r=1
        while r<len(arr):
            minn=min(abs(arr[l]-arr[r]),minn)
            l+=1
            r+=1
        lst=[]
        a=0
        b=1
        while b<len(arr):
            if minn==(abs(arr[a]-arr[b])):
                lst.append([arr[a],arr[b]])
            a+=1
            b+=1
        return lst

        