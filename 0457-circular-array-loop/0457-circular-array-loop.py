class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = i
            direction = nums[i] > 0

            while True:
                ns = next_index(slow)
                nf = next_index(fast)
                nf2 = next_index(nf)

                if (nums[ns] > 0) != direction:
                    break
                if (nums[nf] > 0) != direction:
                    break
                if (nums[nf2] > 0) != direction:
                    break

                slow = ns
                fast = nf2

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            j = i
            while (nums[j] > 0) == direction and nums[j] != 0:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False