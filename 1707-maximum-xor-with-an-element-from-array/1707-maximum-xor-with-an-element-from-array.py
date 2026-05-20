class TrieNode:
    def __init__(self):
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        
        for i in range(31,-1,-1):
            b = (num>>i)&1
            
            if b not in node.child:
                node.child[b] = TrieNode()
            
            node = node.child[b]
    
    def query(self, num):
        node = self.root
        
        if not node.child:
            return -1
        
        ans = 0
        
        for i in range(31,-1,-1):
            b = (num>>i)&1
            want = 1-b
            
            if want in node.child:
                ans |= (1<<i)
                node = node.child[want]
            else:
                node = node.child[b]
        
        return ans

class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        
        q = sorted([(m,x,i) for i,(x,m) in enumerate(queries)])
        
        trie = Trie()
        ans = [-1]*len(queries)
        
        j = 0
        
        for m,x,i in q:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            
            ans[i] = trie.query(x)
        
        return ans