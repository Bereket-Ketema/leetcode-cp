class WordFilter:
    def __init__(self, words):
        self.lookup = {}
        for i, word in enumerate(words):
            for p in range(len(word)+1):
                for s in range(len(word)+1):
                    self.lookup[word[:p] + "#" + word[len(word)-s:]] = i

    def f(self, pref, suff):
        return self.lookup.get(pref + "#" + suff, -1)