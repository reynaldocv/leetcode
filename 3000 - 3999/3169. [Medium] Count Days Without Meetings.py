# https://leetcode.com/problems/count-days-without-meetings/

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        for (start, end) in meetings: 
            counter[start] += 1 
            counter[end + 1] -= 1 
            
        arr = sorted([key for key in counter])
        
        last = 1 
        
        prev = 0        
        ans = 0 
        
        for num in arr:             
            if prev == 0:                
                ans += num - last
                
            prev += counter[num]
            
            last = num 
            
        ans += days - arr[-1] + 1
        
        return ans 
                
        
            
