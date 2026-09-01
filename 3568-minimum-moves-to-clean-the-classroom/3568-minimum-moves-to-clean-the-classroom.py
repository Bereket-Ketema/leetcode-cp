from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litter_id = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        target = (1 << litter_count) - 1

        best = [
            [[-1] * (1 << litter_count) for _ in range(n)]
            for _ in range(m)
        ]

        best[start_r][start_c][0] = energy

        q = deque()
        q.append((start_r, start_c, energy, 0, 0))

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        while q:
            r, c, cur_energy, mask, moves = q.popleft()

            if mask == target:
                return moves

            if cur_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = cur_energy - 1

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter_id[(nr, nc)]
                    new_mask |= 1 << bit

                if new_energy <= best[nr][nc][new_mask]:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1