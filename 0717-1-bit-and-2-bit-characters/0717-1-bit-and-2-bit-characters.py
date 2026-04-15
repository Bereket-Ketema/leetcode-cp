class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        left = 0
        while left < len(bits) - 1:
            if bits[left] == 1:
                left += 2
            else:
                left += 1
        return True if left == len(bits) - 1 else False