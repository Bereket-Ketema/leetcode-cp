class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        even = sorted(
            [d for d in digits if int(d) % 2 == 0],
            reverse=True
        )
        odd = sorted(
            [d for d in digits if int(d) % 2 == 1],
            reverse=True
        )

        e = o = 0

        for i in range(len(digits)):
            if int(digits[i]) % 2 == 0:
                digits[i] = even[e]
                e += 1
            else:
                digits[i] = odd[o]
                o += 1

        return int("".join(digits))