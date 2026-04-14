class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                
                if (num[0] == '0' and i > 1) or (num[i] == '0' and j - i > 1):
                    continue
                
                num1 = int(num[:i])
                num2 = int(num[i:j])
                
                k = j
                while k < n:
                    next_num = num1 + num2
                    next_str = str(next_num)

                    if not num.startswith(next_str, k):
                        break
                    
                    k += len(next_str)
                    num1, num2 = num2, next_num
                
                if k == n:
                    return True
        
        return False