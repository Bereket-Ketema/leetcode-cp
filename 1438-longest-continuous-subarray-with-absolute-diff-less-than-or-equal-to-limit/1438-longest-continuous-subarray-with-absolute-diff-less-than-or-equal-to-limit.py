class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        monoInc = deque()
        monoDec = deque()
        ans = 0
        left = 0

        for right in range(len(nums)):
            
            while monoInc and nums[right] < monoInc[-1]:
                monoInc.pop()
            monoInc.append(nums[right])

            while monoDec and nums[right] > monoDec[-1]:
                monoDec.pop()
            monoDec.append(nums[right]) 

            if monoDec[0] - monoInc[0] > limit:
                if monoDec[0] == nums[left]:
                    monoDec.popleft()
                if monoInc[0] == nums[left]:
                    monoInc.popleft()
                left += 1
            ans = max(ans, right - left + 1)

        return ans