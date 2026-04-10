class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0

        repeat_count = [0] * (n1 + 1)
        next_index = [0] * (n1 + 1)

        j = 0
        cnt = 0

        for k in range(1, n1 + 1):
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        cnt += 1

            repeat_count[k] = cnt
            next_index[k] = j

            for start in range(k):
                if next_index[start] == j:
                    prefix_count = repeat_count[start]

                    pattern_count = (
                        (n1 - start) // (k - start)
                    ) * (repeat_count[k] - repeat_count[start])

                    suffix_count = repeat_count[
                        start + (n1 - start) % (k - start)
                    ] - repeat_count[start]

                    return (prefix_count + pattern_count + suffix_count) // n2

        return repeat_count[n1] // n2