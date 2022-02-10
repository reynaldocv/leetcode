# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def helper(string):
            idx = string.index(":")
            return int(string[:idx])*60 + int(string[idx + 1:])
                       
        start = helper(loginTime)
        end = helper(logoutTime)  

        newStart = start
        if start % 15 != 0: 
            newStart = start + (15 - start % 15)
        
        newEnd = end
        if end % 15 != 0: 
            newEnd = end - (end % 15)
        
        if start <= end: 
            if newEnd >= newStart: 
                return (newEnd - newStart)//15
            else: 
                return 0 
            
        else: 
            return (24*60 - newStart)//15 + newEnd//15
            
        
        
        
