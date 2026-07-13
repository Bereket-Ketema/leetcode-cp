class Solution:
    def countHillValley(self, nums):
        arr = [nums[0]]

        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)

        ans = 0

        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                ans += 1
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                ans += 1

        return ans