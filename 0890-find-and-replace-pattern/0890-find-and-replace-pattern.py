class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(w):
            m1, m2 = {}, {}
            for a, b in zip(w, pattern):
                if m1.get(a, b) != b or m2.get(b, a) != a:
                    return False
                m1[a] = b
                m2[b] = a
            return True
        
        return [w for w in words if match(w)]