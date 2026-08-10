class Solution:
    def calculateTax(self, brackets, income):
        ans = 0
        prev = 0

        for upper, percent in brackets:
            taxable = min(income, upper) - prev

            if taxable > 0:
                ans += taxable * percent / 100

            prev = upper

            if income <= upper:
                break

        return ans