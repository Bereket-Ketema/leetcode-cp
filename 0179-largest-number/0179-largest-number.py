class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return '0'
        for j in range(len(nums)):
            max_ = j
            for i in range(j+1,len(nums)):
                if str(nums[max_])[0] < str(nums[i])[0]:
                    max_ = i
                if str(nums[max_])[0] == str(nums[i])[0]:
                    c1 = str(nums[max_]) + str(nums[i])
                    c2 = str(nums[i]) + str(nums[max_])
                    if int(c1) < int(c2):
                        max_ = i
            nums[j], nums[max_] = nums[max_], nums[j]
        store = ''
        for i in nums:
            store += str(i)
        return store
