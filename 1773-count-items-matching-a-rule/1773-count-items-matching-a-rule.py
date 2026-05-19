class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        mp = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        idx = mp[ruleKey]
        
        return sum(item[idx] == ruleValue for item in items)