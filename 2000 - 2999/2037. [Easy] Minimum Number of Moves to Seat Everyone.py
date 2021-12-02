# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        ans = 0 
        n = len(students)
        
        for i in range(n):
            ans += abs(students[i] - seats[i])
        
        return ans
        
