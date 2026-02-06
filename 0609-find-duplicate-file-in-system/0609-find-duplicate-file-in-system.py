from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
      output = []
      store = defaultdict(list)
      for path in paths:
        file = path.split(" ")
        for i in range(1,len(file)):
          index1 = file[i].find("(")
          index2 = file[i].find(")")
          store[file[i][index1+1:index2]].append(file[0] + "/"+ file[i][:index1])
      for v in store.values():
        if len(v) > 1:
          output.append(v)
      return output