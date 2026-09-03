class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        next_char = ord('a')

        for c in key:
            if c != ' ' and c not in mapping:
                mapping[c] = chr(next_char)
                next_char += 1

        result = []

        for c in message:
            if c == ' ':
                result.append(' ')
            else:
                result.append(mapping[c])

        return ''.join(result)