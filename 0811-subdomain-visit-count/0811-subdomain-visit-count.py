from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        output = []
        frequency = defaultdict(int)
        for sent in cpdomains:
          r, s = sent.split(" ")
          frequency[s] += int(r)
          
          while s.find(".") != -1:
            index = s.find(".")
            frequency[s[index+1:]] += int(r)
            s = s[index+1:]
        for k,v in frequency.items():
          output.append(str(v)+ " "+ k)
        return output