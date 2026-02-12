from collections import Counter
class Solution:
  def findCommonResponse(self, responses: list[list[str]]) -> str:
    store = []
    for _ in range(len(responses)):
      s = set(responses[_])
      store.extend(s)
    freq = Counter(store)
    
    mx = max(freq.values())

    return min(k for k,v in freq.items() if v == mx)