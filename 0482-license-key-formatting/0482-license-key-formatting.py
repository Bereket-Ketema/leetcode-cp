class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        
        result = []
        count = 0
        
        for ch in reversed(s):
            result.append(ch)
            count += 1
            
            if count == k:
                result.append('-')
                count = 0
        
        result = ''.join(result[::-1])
        
        if result and result[0] == '-':
            result = result[1:]
        
        return result