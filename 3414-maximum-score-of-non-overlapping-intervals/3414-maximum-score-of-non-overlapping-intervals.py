class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted((intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n))
        
        starts = [x[0] for x in arr]
        next_pos = []
        for i in range(n):
            next_pos.append(bisect_right(starts, arr[i][1]))

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            wt, idx = arr[i][2], arr[i][3]
            nxt = next_pos[i]
            for k in range(1, 5):
                skip_val, skip_idxs = dp[i + 1][k]
                
                take_val, take_idxs = dp[nxt][k - 1]
                take_val += wt
                new_idxs = sorted(take_idxs + [idx])
                
                if take_val > skip_val:
                    dp[i][k] = (take_val, new_idxs)
                elif take_val == skip_val:
                    if not skip_idxs or (new_idxs and new_idxs < skip_idxs):
                        dp[i][k] = (take_val, new_idxs)
                    else:
                        dp[i][k] = (skip_val, skip_idxs)
                else:
                    dp[i][k] = (skip_val, skip_idxs)

        best_val = -1
        best_idxs = []
        for k in range(1, 5):
            val, idxs = dp[0][k]
            if val > best_val:
                best_val = val
                best_idxs = idxs
            elif val == best_val:
                if idxs < best_idxs:
                    best_idxs = idxs

        return best_idxs