class Solution:
    def isAlienSorted(self, words, order):
        pos = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]

            for j in range(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    if pos[w1[j]] > pos[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True