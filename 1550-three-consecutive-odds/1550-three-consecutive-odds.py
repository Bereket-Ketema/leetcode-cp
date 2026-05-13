class Solution:
    def threeConsecutiveOdds(self, arr):
        cnt = 0

        for x in arr:
            if x % 2:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0

        return False