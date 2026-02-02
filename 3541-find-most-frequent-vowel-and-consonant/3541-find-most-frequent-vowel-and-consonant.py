class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqv = {}
        freqc = {}
        vowel = 'aeiou'
        for letter in s:
            if letter in vowel:
                if letter not in freqv:
                    freqv[letter] = 1
                else:
                    freqv[letter] += 1
            else:
                if letter not in freqc:
                    freqc[letter] = 1
                else:
                    freqc[letter] += 1

        return max(freqc.values() if freqc else [0]) + max(freqv.values() if freqv else [0])