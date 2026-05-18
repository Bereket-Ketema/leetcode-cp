class Solution:
    def lengthLongestPath(self, input):
        stack = {0:0}
        ans = 0
        
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                ans = max(ans, stack[depth] + len(name))
            else:
                stack[depth+1] = stack[depth] + len(name) + 1
        
        return ans