class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        check = []
        for i in range(1, len(words)):
            if i == 1:
                freq1 = Counter(words[i - 1])
                a = set(words[i - 1])
            else:
                freq1 = Counter(check)
                a = set(check)
            freq2 = Counter(words[i])
            b = set(words[i])

            hello = a.intersection(b)
            check.clear()
            for i in hello:
                yes = i * min(freq1[i], freq2[i])
                check.extend(list(i * min(freq1[i], freq2[i])))
        return check
