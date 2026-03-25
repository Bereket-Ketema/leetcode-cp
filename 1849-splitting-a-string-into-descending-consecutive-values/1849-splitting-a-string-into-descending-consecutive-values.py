class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(idx, current):
            if idx == len(s):
                #check if current is valid
                for i in range(1, len(current)):
                    if current[i - 1] - current[i] != 1:
                        return False
                return len(current) >= 2

            for j in range(idx, len(s)):
                val = int(s[idx: j + 1])
                current.append(val)
                if backtrack(j + 1, current):
                    return True
                current.pop()
        
            return False
        return backtrack(0, [])
          