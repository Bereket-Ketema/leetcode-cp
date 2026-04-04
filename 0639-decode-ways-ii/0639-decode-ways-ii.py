class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        n = len(s)
        dp0 = 1  
        dp1 = 0 
        
        if s[0] == '*':
            dp1 = 9
        elif s[0] == '0':
            dp1 = 0
        else:
            dp1 = 1
        
        for i in range(1, n):
            dp2 = 0
            
            if s[i] == '*':
                dp2 += 9 * dp1
            elif s[i] != '0':
                dp2 += dp1
            
            if s[i-1] == '*':
                if s[i] == '*':
                    dp2 += 15 * dp0 
                elif '0' <= s[i] <= '6':
                    dp2 += 2 * dp0  
                else:
                    dp2 += dp0       
            else:
                if s[i] == '*':
                    if s[i-1] == '1':
                        dp2 += 9 * dp0
                    elif s[i-1] == '2':
                        dp2 += 6 * dp0
                else:
                    if 10 <= int(s[i-1:i+1]) <= 26:
                        dp2 += dp0
            
            dp2 %= MOD
            dp0, dp1 = dp1, dp2
        
        return dp1