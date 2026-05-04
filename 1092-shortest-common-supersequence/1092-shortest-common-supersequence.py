class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        m, n = len(str1), len(str2)

        # LCS DP
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # Build answer
        i = j = 0
        res = []

        while i < m and j < n:
            if str1[i] == str2[j]:
                res.append(str1[i])
                i += 1
                j += 1
            elif dp[i+1][j] >= dp[i][j+1]:
                res.append(str1[i])
                i += 1
            else:
                res.append(str2[j])
                j += 1

        res.append(str1[i:])
        res.append(str2[j:])

        return "".join(res)