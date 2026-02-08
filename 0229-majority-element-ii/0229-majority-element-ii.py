from collections import Counter
class Solution:
  def majorityElement(self, nums: list[int]) -> list[int]:
    freq = Counter(nums)
    store = set(nums) 
    return [item for item in store if freq[item] > len(nums)/3]