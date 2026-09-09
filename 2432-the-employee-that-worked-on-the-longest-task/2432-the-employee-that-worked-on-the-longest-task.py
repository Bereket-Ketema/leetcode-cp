class Solution:
    def hardestWorker(self, n, logs):
        hardest_id = logs[0][0]
        max_time = logs[0][1]

        previous_time = logs[0][1]

        for i in range(1, len(logs)):
            employee_id, leave_time = logs[i]

            duration = leave_time - previous_time

            if duration > max_time:
                max_time = duration
                hardest_id = employee_id
            elif duration == max_time:
                hardest_id = min(hardest_id, employee_id)

            previous_time = leave_time

        return hardest_id