class Solution:
    def oddString(self, words: list[str]) -> str:
        def diff(word):
            return tuple(ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))

        first = diff(words[0])
        second = diff(words[1])

        if first != second:
            if first == diff(words[2]):
                return words[1]
            return words[0]

        for i in range(2, len(words)):
            if diff(words[i]) != first:
                return words[i]

        return ""