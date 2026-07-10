class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 1
        ans = ''
        for i in range(1, len(num)):
            if num[i] == num[i - 1] and num[i] != 0:
                    count += 1
            else:
                count = 1

            if count == 3:
                if ans:
                    ans = str(max(int(ans), int(num[i])))
                else:
                    ans = num[i]
                
                count = 1
        
        return ans * 3