class Solution:
    def generateTag(self, caption: str) -> str:
        result = "#"
        store = list(caption.split())
        if len(store) == 0:
            return result
        result = result + store[0][0].lower() + store[0][1:].lower()
        for i in range(1,len(store)):
            result += store[i][0].upper() + store[i][1:].lower()
        return result if len(result) < 100 else result[:100]