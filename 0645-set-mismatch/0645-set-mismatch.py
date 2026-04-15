class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        ans = []
        freq = Counter(nums)
        check = set(nums)

        for k, v in freq.items():
            if v == 2:
                ans.append(k)
                break
        
        for i in range(1, len(nums) + 1):
            if i not in check:
                ans.append(i)
                break
        return ans