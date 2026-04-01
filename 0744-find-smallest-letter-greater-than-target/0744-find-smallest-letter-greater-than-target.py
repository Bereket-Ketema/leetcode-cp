class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        small = -1
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                small = letters[mid]
                right = mid - 1
        return small
