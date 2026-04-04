from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()

                if pos == target:
                    return steps

                new_pos = pos + speed
                new_speed = speed * 2
                state = (new_pos, new_speed)
                
                if 0 <= new_pos <= 2 * target and state not in visited:
                    visited.add(state)
                    queue.append(state)

                new_speed = -1 if speed > 0 else 1
                state = (pos, new_speed)
                
                if state not in visited:
                    visited.add(state)
                    queue.append(state)

            steps += 1