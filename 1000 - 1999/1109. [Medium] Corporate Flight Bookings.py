# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for (first, last, seats) in bookings: 
            counter[first] += seats
            counter[last + 1] -= seats
            
        prev = 0 
        
        ans = []
        
        for i in range(1, n + 1):
            prev += counter[i]
            
            ans.append(prev)
            
        return ans 
