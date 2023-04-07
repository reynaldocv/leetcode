# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        month = {}
        
        for i in range(12):
            if i < 9: 
                month[months[i]] = "0" + str(i + 1)
            
            else: 
                month[months[i]] = str(i + 1)
            
        
        date = date.split(" ")
        
        if len(date[0]) == 3: 
            date[0] = "0" + date[0][0]
        
        else: 
            date[0] = date[0][0] + date[0][1]
            
        ans = date[2] + "-" + month[date[1]] + "-" + date[0]
        
        return ans 
        
        
