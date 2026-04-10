from collections import deque

class Solution:
    def kSimilarity(self, s1, s2):
        queue = deque([(s1, 0)])
        visited = {s1}
        
        while queue:
            s, steps = queue.popleft()
            if s == s2:
                return steps
            
            i = 0
            while s[i] == s2[i]:
                i += 1
            
            for j in range(i+1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    lst = list(s)
                    lst[i], lst[j] = lst[j], lst[i]
                    new_s = ''.join(lst)
                    
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append((new_s, steps+1))