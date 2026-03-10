class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        deff = [0] * (n + 1)

        for l, r, val in bookings:
            deff[l-1] += val
            deff[r] -= val
        
        arr = [0] * n
        arr[0] = deff[0]
        for i in range(1,len(arr)):
            arr[i] = arr[i-1] + deff[i]
        
        return arr