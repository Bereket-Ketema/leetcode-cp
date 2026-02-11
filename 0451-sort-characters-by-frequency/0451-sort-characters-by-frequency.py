from collections import Counter
class Solution:
  def frequencySort(self, s: str) -> str:
    freq = Counter(s)
    sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
    store = ""
    for k,v in sorted_dict.items():
      store += k*v
    return store