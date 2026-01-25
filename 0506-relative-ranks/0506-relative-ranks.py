class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        abebe = []
        for i in range(len(score)):
            abebe.append((score[i], i))
        abebe.sort(reverse=True)
        
        for i in range(len(score)):
            if i == 0:
                score[abebe[i][1]] = "Gold Medal"
            elif i == 1:
                score[abebe[i][1]] = "Silver Medal"
            elif i == 2:
                score[abebe[i][1]] = "Bronze Medal"
            else:
                score[abebe[i][1]] = str(i+1)
        return score