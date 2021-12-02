# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        date = date.split("-")
        
        daysth = 0
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        
        for i in range(month):
            daysth += daysOfMonth[i]
        if month > 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                daysth += 1
        
        return daysth + day
            
