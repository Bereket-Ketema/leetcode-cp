class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_id = {s:i for i,s in enumerate(req_skills)}
        n = len(req_skills)

        dp = {0:[]}

        for i,p in enumerate(people):
            mask = 0
            for s in p:
                if s in skill_id:
                    mask |= (1<<skill_id[s])

            for old_mask,team in list(dp.items()):
                new_mask = old_mask | mask

                if new_mask == old_mask:
                    continue

                if new_mask not in dp or len(dp[new_mask]) > len(team)+1:
                    dp[new_mask] = team+[i]

        return dp[(1<<n)-1]