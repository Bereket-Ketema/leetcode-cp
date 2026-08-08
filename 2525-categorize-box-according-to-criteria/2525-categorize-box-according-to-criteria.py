class Solution:
    def categorizeBox(self, length, width, height, mass):
        bulky = (
            length >= 10**4 or
            width >= 10**4 or
            height >= 10**4 or
            length * width * height >= 10**9
        )

        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"

        return "Neither"