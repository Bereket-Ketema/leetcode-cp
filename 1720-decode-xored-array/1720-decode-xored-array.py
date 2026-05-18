class Solution:
    def decode(self, encoded, first):
        arr = [first]
        
        for x in encoded:
            arr.append(arr[-1] ^ x)
        
        return arr