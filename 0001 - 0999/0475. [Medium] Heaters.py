# https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        m = len(heaters)        
        heaters.sort()
        ans = 0    
        for house in houses:
            idx = bisect_left(heaters, house)
            if idx == m: 
                ans = max(ans, abs(house - heaters[-1]))
            elif idx == 0: 
                ans = max(ans, abs(house - heaters[0]))
            else: 
                aux = min(abs(house - heaters[idx]), abs(house - heaters[idx - 1]))
                ans = max(ans, aux)
                
        return ans
        
     
            
        
        
