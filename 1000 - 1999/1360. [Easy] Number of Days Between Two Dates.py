# https://leetcode.com/problems/number-of-days-between-two-dates/

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def NumberOfDays(day, month, year):
            dayspermonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
            days = 0
            years = year - 1 - 1900
            leapyears = years // 4 + 1
            days += (years - leapyears)*365
            days += leapyears*366
            
            for i in range(month):
                days += dayspermonth[i]
            
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if month > 2:
                    day += 1
                
            days += day
            
            return days
        
        date1 = date1.split("-")
        date2 = date2.split("-")
        days1 = NumberOfDays(int(date1[2]), int(date1[1]), int(date1[0]))
        days2 = NumberOfDays(int(date2[2]), int(date2[1]), int(date2[0]))
            
        return abs(days2 - days1)
