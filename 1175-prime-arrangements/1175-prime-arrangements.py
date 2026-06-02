class Solution:
    def numPrimeArrangements(self, n):
        MOD = 10**9 + 7

        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        primes = sum(isPrime(i) for i in range(1, n + 1))

        def fact(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

        return (fact(primes) * fact(n - primes)) % MOD