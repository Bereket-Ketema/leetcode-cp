class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        def check(k: int) -> bool:
            prev_max = -1
            for start in range(0, n, k):
                sub = nums[start : start + k]
                drops = [i for i in range(k) if sub[i] > sub[(i + 1) % k]]
                
                if not drops:
                    cur_min = min(sub)
                    cur_max = max(sub)
                elif len(drops) == 1:
                    d = drops[0]
                    cur_min = sub[(d + 1) % k]
                    cur_max = sub[d]
                else:
                    return False
                
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                
            return True

        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)

        return sum(k for k in divisors if check(k))