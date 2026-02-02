class Solution:
    def minimumFlips(self, n: int) -> int:
        count = 0
        target = bin(n)[2:]
        for i in range(len(target)):
            if target[i] != target[::-1][i]:
                count +=1
        return count