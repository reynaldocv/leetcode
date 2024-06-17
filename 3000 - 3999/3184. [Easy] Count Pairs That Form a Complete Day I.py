# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for hour in hours: 
            counter[hour % 24] += 1 
            
        ans = 0 
        
        for key in counter: 
            if key == 0 or key == 12: 
                ans += counter[key]*(counter[key] - 1)
                
            elif key in counter and (24 - key) in counter: 
                ans += counter[key]*counter[24 - key]
                
        return ans//2
