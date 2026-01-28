class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = "".join(set(ransomNote))
        for i in range(len(result)):
            if result[i] not in magazine or ransomNote.count(result[i]) > magazine.count(result[i]):
                return False
        return True