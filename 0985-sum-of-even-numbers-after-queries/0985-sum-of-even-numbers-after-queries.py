class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
            store = []
            even = 0
            for i in nums:
              if i % 2 == 0:
                even += i
            for _, v in enumerate(queries):
                if nums[v[1]] % 2 == 0:
                    even -= nums[v[1]]
                nums[v[1]] += v[0]
                if nums[v[1]] % 2 == 0:
                    even += nums[v[1]]
                store.append(even)
            return store