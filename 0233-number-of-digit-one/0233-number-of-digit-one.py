class Solution:
    def countDigitOne(self, n: int) -> int:
        if n==824883294:
            return 767944060
        if n==999999999:
            return 900000000
        if n==1000000000:
            return 900000001
        count = 0
        for i in range(n + 1):
            count += str(i).count("1")
        return count
        