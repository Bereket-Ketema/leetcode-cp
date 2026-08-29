class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_h, cur_m = map(int, current.split(':'))
        cor_h, cor_m = map(int, correct.split(':'))

        diff = (cor_h * 60 + cor_m) - (cur_h * 60 + cur_m)
        ops = 0

        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step

        return ops