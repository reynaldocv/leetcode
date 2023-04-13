# https://leetcode.com/problems/day-of-the-week/

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
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
        
        labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        
        for i in range(1, 12):
            days[i] += days[i - 1]
        
        days = helper(day, month, year) 
        
        return labels[days % 7]
