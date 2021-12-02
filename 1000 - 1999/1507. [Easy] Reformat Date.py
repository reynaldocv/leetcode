# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        mes = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dic = {}
        for i in range(12):
            if i < 9:
                dic[mes[i]] = "0" + str(i + 1)
            else:
                dic[mes[i]] = str(i + 1)
            
        date = date.split(" ")
        ans = date[2] + "-" + dic[date[1]] + "-"
        day = date[0][0:len(date[0]) - 2]
        if len(day) == 1:
            day = "0" + day
        ans += day
        return ans
        
