class Solution:
    def isPrime(self,n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        n = len(nums)
        maxPrime = 0

        for i in range(n):
            if self.isPrime(nums[i][i]):
                maxPrime = max(maxPrime, nums[i][i])

            if self.isPrime(nums[i][n - 1 - i]):
                maxPrime = max(maxPrime, nums[i][n - 1 - i])
        return maxPrime
