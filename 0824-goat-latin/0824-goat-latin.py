class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        store = sentence.split()
        vowel = "aeiouAEIOU"
        for i in range(len(store)):
            print(store[i])
            if store[i][0] in vowel:
                store[i] = store[i] + "ma" + ("a" * (i+1))
            else:
                temp = list(store[i])
                temp.append(temp[0])
                temp.pop(0)
                store[i] = "".join(temp) + "ma" + ("a" * (i+1))
        return " ".join(store)