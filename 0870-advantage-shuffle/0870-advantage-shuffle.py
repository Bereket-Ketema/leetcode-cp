class Solution:
    def advantageCount(self, nums1, nums2):
        import heapq
        
        nums1.sort()
        maxheap = [(-v, i) for i, v in enumerate(nums2)]
        heapq.heapify(maxheap)
        
        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1
        
        while maxheap:
            val, i = heapq.heappop(maxheap)
            val = -val
            
            if nums1[right] > val:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        
        return res