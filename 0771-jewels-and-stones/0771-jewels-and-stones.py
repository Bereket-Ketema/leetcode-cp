class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        count = 0
        for i in range(len(stones)):
            if stones[i] not in freq:
                freq[stones[i]] = 1
            else:
                freq[stones[i]] +=1
        for k,v in freq.items():
            if k in jewels:
                count += v
        return count