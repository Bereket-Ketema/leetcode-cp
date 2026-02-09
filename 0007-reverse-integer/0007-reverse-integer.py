class Solution:
    def reverse(self, x: int) -> int:
        if x > 0 and int(str(x)[::-1]) <= pow(2,31)-1:
            return int(str(x)[::-1])
        elif x < 0 and int(str(x)[0]+str(x)[:0:-1]) >= pow(-2,31):
            return int(str(x)[0]+str(x)[:0:-1])
        else:
            return 0        