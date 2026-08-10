class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lower = upper = digit = special = False
        specials = "!@#$%^&*()-+"

        for i, ch in enumerate(password):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if ch.islower():
                lower = True
            elif ch.isupper():
                upper = True
            elif ch.isdigit():
                digit = True
            elif ch in specials:
                special = True

        return lower and upper and digit and special