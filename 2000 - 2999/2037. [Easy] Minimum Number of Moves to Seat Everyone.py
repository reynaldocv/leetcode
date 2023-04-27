# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        
        seats.sort() 
        students.sort() 
        
        ans = 0 
        
        for i in range(n):
            ans += abs(seats[i] - students[i])
            
        return ans 
        
