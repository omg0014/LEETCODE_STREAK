class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for c in range(1, n + 1):
            c2 = c * c
            for a in range(1, n + 1):
                b2 = c2 - a * a
                if b2 <= 0:
                    continue
                b = int(math.isqrt(b2))
                if b * b == b2 and 1 <= b <= n:
                    cnt += 1
        return cnt

        
        