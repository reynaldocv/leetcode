# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        start = int(current[: 2])*60 + int(current[3: ])
        end = int(correct[: 2])*60 + int(correct[3: ])
        
        diff = end - start
        
        ans = 0 
        
        for k in [60, 15, 5, 1]:
            ans += (diff//k)
            
            diff = diff % k 
            
        return ans 

