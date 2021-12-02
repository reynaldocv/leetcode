# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        minDays = [0]*n
        minDays[0] = 0 
        MOD = 10**9 + 7
        for i in range(1, n):
            minDays[i] = 2*minDays[i - 1] - minDays[nextVisit[i - 1]] + 2
            minDays[i] %= MOD
            
        return minDays[n - 1]
        
        
