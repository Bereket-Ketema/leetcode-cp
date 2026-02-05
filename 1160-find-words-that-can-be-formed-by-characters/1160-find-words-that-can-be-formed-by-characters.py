from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
      count = 0
      chars_freq = Counter(chars)
      for word in words:
        words_freq = Counter(word)
        check = True

        for k in words_freq.keys():
          if not( words_freq[k] <= chars_freq.get(k,0)):
            check = False
            break
        if check:
          count += len(word)
      return count