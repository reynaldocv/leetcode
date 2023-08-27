# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for t in time: 
            counter[t % 60] += 1 
            
        ans = 0 
            
        for key in counter: 
            if key == 0 or key == 30: 
                ans += (counter[key] - 1)*counter[key]//2
                
            elif key < 30 and (60 - key) in counter: 
                ans += counter[key]*counter[60 - key]
                
        return ans 
        
            
        
