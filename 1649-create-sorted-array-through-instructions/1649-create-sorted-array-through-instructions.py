from typing import List

class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [[0, 0] for _ in range(n)]  # [smaller, greater]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            
            # Count greater (right to left)
            l, r = len(left) - 1, len(right) - 1
            while l >= 0 and r >= 0:
                if nums[left[l]] <= nums[right[r]]:
                    ans[right[r]][1] += (len(left) - 1 - l)
                    r -= 1
                else:
                    l -= 1

            while r >= 0:
                ans[right[r]][1] += len(left)
                r -= 1

            # Count smaller (left to right)
            l = r = 0
            while l < len(left) and r < len(right):
                if nums[left[l]] < nums[right[r]]:
                    res.append(left[l])
                    l += 1
                else:
                    ans[right[r]][0] += l
                    res.append(right[r])
                    r += 1

            while r < len(right):
                ans[right[r]][0] += l
                res.append(right[r])
                r += 1

            res.extend(left[l:])
            return res

        merge_sort(list(range(n)))

        MOD = 10**9 + 7
        return sum(min(x, y) for x, y in ans) % MOD
