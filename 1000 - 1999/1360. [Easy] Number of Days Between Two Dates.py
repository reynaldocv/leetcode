# https://leetcode.com/problems/number-of-days-between-two-dates/

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def helper(day, month, year):
            ans = day
            
            years = year - 1 - 1900
            
            leapYears = years // 4 + 1
            
            ans += (years - leapYears)*365            
            ans += leapYears*366
            
            ans += days[month - 1]
            
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if month > 2:
                    ans += 1
                            
            return ans
        
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        
        for i in range(1, 12):
            days[i] += days[i - 1]
        
        date1 = date1.split("-")
        date2 = date2.split("-")
        
        days1 = helper(int(date1[2]), int(date1[1]), int(date1[0]))
        days2 = helper(int(date2[2]), int(date2[1]), int(date2[0]))
            
        return abs(days2 - days1)
