# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count, counter = {}, {}
        for s in "balloon":
            count[s] = count.get(s, 0) + 1
            
        for s in text: 
            counter[s] = counter.get(s, 0) + 1
        
        ans = counter.get("b", 0); 
        for s in "balloon":
            ans = min(ans, counter.get(s, 0)//count.get(s, 1))
        return ans
            
            
