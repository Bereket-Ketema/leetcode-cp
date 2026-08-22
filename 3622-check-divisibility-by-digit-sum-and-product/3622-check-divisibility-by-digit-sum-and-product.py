class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = sum(map(int, str(n)))
        m = math.prod(map(int, str(n)))

        if n % (s + m) == 0:
            return True

        return False