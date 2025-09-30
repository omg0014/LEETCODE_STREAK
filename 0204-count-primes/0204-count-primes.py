class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[0]*(n)
        if n==1 or n==0:
            return 0
        primes[0] = 1
        primes[1] = 1
        for i in range(2,n):
            for j in range(i*i,n,i):
                primes[j]=1
        c=0
        for i in range(n):
            if primes[i]==0:
                c+=1
        return c