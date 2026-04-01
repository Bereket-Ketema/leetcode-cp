class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(capacity, weights):
            day = 1
            cur_sum = 0
            for weight in weights:
                if weight + cur_sum > capacity:
                    day += 1
                    cur_sum = weight
                else:
                    cur_sum += weight

            return day <= days

        ans, left, right = -1,  max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid, weights):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans