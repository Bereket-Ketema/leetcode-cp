class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == endGene:
                return steps
            
            for i in range(len(curr)):
                for g in genes:
                    if g != curr[i]:
                        new_gene = curr[:i] + g + curr[i+1:]
                        
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            queue.append((new_gene, steps + 1))
        
        return -1