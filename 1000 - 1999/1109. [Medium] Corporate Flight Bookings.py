# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = defaultdict(lambda: 0)
        for (first, last, cnt) in bookings: 
            seats[first] += cnt
            seats[last + 1] -= cnt
            
        ans = [0 for i in range(n)]
        
        prev = 0 
        for i in range(1, n + 1):
            ans[i - 1] = prev + seats[i]
            prev = ans[i - 1]
            
        return ans
