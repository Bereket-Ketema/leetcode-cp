import heapq

class Solution:
    def getOrder(self, tasks):
        arr = []
        for i, (e, p) in enumerate(tasks):
            arr.append((e, p, i))

        arr.sort()

        ans = []
        heap = []
        time = 0
        i = 0
        n = len(arr)

        while i < n or heap:
            if not heap and time < arr[i][0]:
                time = arr[i][0]

            while i < n and arr[i][0] <= time:
                heapq.heappush(heap, (arr[i][1], arr[i][2]))
                i += 1

            p, idx = heapq.heappop(heap)
            ans.append(idx)
            time += p

        return ans