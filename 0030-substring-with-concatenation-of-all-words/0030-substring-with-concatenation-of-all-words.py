class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            current_count = {}
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        result.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = right + word_len

        return result