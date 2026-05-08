class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []

        for word in words:
            node = self.root
            for c in reversed(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.end = True

    def query(self, letter):
        self.stream.append(letter)
        node = self.root

        for c in reversed(self.stream):
            if c not in node.children:
                return False
            node = node.children[c]
            if node.end:
                return True

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)