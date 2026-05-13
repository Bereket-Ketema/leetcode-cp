class Solution:
    def countStudents(self, students, sandwiches):
        from collections import Counter
        
        c = Counter(students)

        for s in sandwiches:
            if c[s] == 0:
                break
            c[s] -= 1

        return c[0] + c[1]