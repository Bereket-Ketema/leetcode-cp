from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        coins = list(set(coins))

        useful = []

        for i, x in enumerate(coins):
            redundant = False

            for j, y in enumerate(coins):
                if i != j and x % y == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(x)

        coins = useful

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            valid = False
                            break

                if not valid:
                    continue

                value = x // multiple

                if bits % 2:
                    total += value
                else:
                    total -= value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left