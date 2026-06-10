class Solution:
    def numDifferentIntegers(self, word):
        cur = ""
        nums = set()

        for ch in word:
            if ch.isdigit():
                cur += ch
            else:
                if cur:
                    nums.add(str(int(cur)))
                    cur = ""

        if cur:
            nums.add(str(int(cur)))

        return len(nums)