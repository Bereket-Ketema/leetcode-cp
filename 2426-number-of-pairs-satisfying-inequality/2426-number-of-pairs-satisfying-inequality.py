class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = [a - b for a, b in zip(nums1, nums2)]
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, count_left = merge_sort(nums[:mid])
            right, count_right = merge_sort(nums[mid:])
            
            count = count_left + count_right
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                count += len(right) - j
            
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
        
        _, result = merge_sort(arr)
        return result