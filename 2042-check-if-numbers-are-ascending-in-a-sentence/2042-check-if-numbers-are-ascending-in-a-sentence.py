class Solution:
    def areNumbersAscending(self, s):
        prev = -1

        for word in s.split():
            if word.isdigit():
                num = int(word)
                if num <= prev:
                    return False
                prev = num

        return True