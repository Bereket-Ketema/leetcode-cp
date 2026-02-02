class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Step 1: Build frequency map of license plate
        freq = {}
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                freq[i] = freq.get(i, 0) + 1
        
        shortest_word = ""
        
        # Step 2: Check each word
        for word in words:
            temp = {}
            for letter in word:
                temp[letter] = temp.get(letter, 0) + 1
            
            # Step 3: Check if word satisfies license plate
            valid = True
            for char, count in freq.items():
                if temp.get(char, 0) < count:
                    valid = False
                    break
            
            # Step 4: Update shortest_word
            if valid:
                if shortest_word == "" or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word
