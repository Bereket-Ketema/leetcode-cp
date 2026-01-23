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
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        count = []
        for i in nums:
            if nums.count(i) >1 and self.isPrime(nums.count(i)):
                return True
        return False