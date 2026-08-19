class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        answer = (n - len(rows)) * 2

        for seats in rows.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if not (seats & left) and not (seats & right):
                answer += 2

            elif not (seats & left):
                answer += 1

            elif not (seats & middle):
                answer += 1

            elif not (seats & right):
                answer += 1

        return answer