from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Step 1: BFS to build parents map
        parents = defaultdict(list)
        level = {beginWord}
        visited = set([beginWord])
        found = False
        
        while level and not found:
            next_level = set()
            local_visited = set()
            
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in wordSet and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            
                            if new_word not in local_visited:
                                next_level.add(new_word)
                                local_visited.add(new_word)
                            
                            parents[new_word].append(word)
            
            visited |= local_visited
            level = next_level
        
        # Step 2: Backtrack to build paths
        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for p in parents[word]:
                dfs(p, path + [p])
        
        if found:
            dfs(endWord, [endWord])
        
        return res