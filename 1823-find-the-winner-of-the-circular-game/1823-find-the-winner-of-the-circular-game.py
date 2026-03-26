class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = list(range(1, n + 1))
        idx = 0

        while len(people) > 1:
            idx = (idx + k - 1) % len(people)
            people.pop(idx)

        return people[0]