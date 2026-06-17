class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        store = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
        
        def calc(nums):
            value = ''

            for i in range(len(nums)):
                value += str(store[nums[i]])
            
            return int(value)
        
        return True if calc(firstWord) + calc(secondWord) == calc(targetWord) else False