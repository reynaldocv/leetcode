# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxElem = 0         
        cnt = 0
        
        ans = 0 
        
        for num in flips: 
            cnt += 1 
            maxElem = max(maxElem, num)
            
            if cnt == maxElem: 
                ans += 1 
                
        return ans 
  
