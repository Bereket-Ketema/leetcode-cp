class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:]
        nums = ''
        for i in range(len(n)):
            if n[i] == str(0):
                nums += str(1)
            else:
                nums += str(0)
        return int(nums,2)