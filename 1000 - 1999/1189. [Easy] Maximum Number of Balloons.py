# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(lambda: 0)
        
        cnt = defaultdict(lambda: 0)
        
        for char in "balloon":
            counter[char] += 1 
            
        for char in text: 
            if char in counter: 
                cnt[char] += 1 
                
        if len(cnt) != 5: 
            return 0 
        
        ans = inf 
        
        for char in "balloon":
            ans = min(ans, cnt[char]//counter[char])
            
        return ans 
