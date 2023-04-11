# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        year = int(date[: 4])
        month = int(date[5: 7])
        day = int(date[8: ])
        
        for i in range(1, 12):
            days[i] += days[i - 1]
            
        ans = day
        
        if month >= 3:
            if year % 4 == 0:
                if year % 100 == 0:                    
                    if year % 400 == 0: 
                        ans += 1 
                
                else: 
                    ans += 1 
            
        ans += days[month - 1] 
        
        return ans 
        
        
            
