# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        counterAbsent = 0 
        counterLate = 0 
        maxLate = 0 
        
        for char in s: 
            if char == "L":
                counterLate += 1 
                maxLate = max(maxLate, counterLate)
            
            else:                 
                if char == "A":
                    counterAbsent += 1 
                    
                counterLate = 0 
                
        return maxLate < 3 and counterAbsent < 2 
        
