class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        abebe = score.copy()
        abebe.sort(reverse=True)
        print(abebe)
        for i in range(len(score)):
            if i == 0:
                score[score.index(abebe[0])] = "Gold Medal"
            elif i == 1:
                score[score.index(abebe[1])] = "Silver Medal"
            elif i == 2:
                score[score.index(abebe[2])] = "Bronze Medal"
            else:
                score[score.index(abebe[i])] = "{}".format(i+1)
        return score