import heapq

class Solution:
    def smallestRange(self, nums):
        k = len(nums)
        heap = []
        current_max = float('-inf')
        
        for i in range(k):
            val = nums[i][0]
            heap.append((val, i, 0))
            current_max = max(current_max, val)
        
        heapq.heapify(heap)
        best_range = [float('-inf'), float('inf')]
        
        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            
            if current_max - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, current_max]
            
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        
        return best_range