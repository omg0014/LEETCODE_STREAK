class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        close = [-1, -1]

        # sieve
        primes = [0] * (right + 1)
        if right >= 1:
            primes[0] = primes[1] = 1
        for i in range(2, int(right**0.5) + 1):
            if primes[i] == 0:
                for j in range(i * i, right + 1, i):
                    primes[j] = 1

        lst = [i for i in range(left, right + 1) if primes[i] == 0]

        if len(lst) < 2:   
            return close

        minn = float("inf")
        for i in range(len(lst) - 1):
            diff = lst[i + 1] - lst[i]
            if diff < minn:
                minn = diff
                close = [lst[i], lst[i + 1]]

        return close
