class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if int(sqrt(mid)) == int(sqrt(x)):
                return int(sqrt(mid))

            elif int(sqrt(mid)) < int(sqrt(x)):
                left = mid + 1

            else:
                right = mid - 1
