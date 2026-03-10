class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        stack = []
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                store[stack.pop()] = num
            stack.append(num)
        
        for num in stack:
            store[num] = -1
        
        return [store[num] for num in nums1]
