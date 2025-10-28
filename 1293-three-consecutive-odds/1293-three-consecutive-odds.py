class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        f=0
        while f<len(arr)-2:
            if arr[f]%2!=0 and arr[f+1]%2!=0 and arr[f+2]%2!=0:
                return True
            f+=1
        return False

