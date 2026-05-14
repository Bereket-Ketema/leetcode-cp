class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pick(nums, k):
            drop = len(nums) - k
            stack = []
            
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            
            return stack[:k]
        
        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        
        ans = []
        
        for i in range(max(0, k-len(nums2)), min(k, len(nums1)) + 1):
            a = pick(nums1, i)
            b = pick(nums2, k-i)
            ans = max(ans, merge(a[:], b[:]))
        
        return ans