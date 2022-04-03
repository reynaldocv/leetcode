# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def helper(string):
            return int(string[:2])*60 + int(string[3:])
        
        start = helper(current)
        end = helper(correct)
        
        diff = end - start 
        
        ans = 0 
        
        for value in [60, 15, 5, 1]:
            while diff >= value: 
                ans += 1 
                diff -= value
                
        return ans 
            

