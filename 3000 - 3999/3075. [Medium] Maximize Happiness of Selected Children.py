# https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        
        for num in happiness: 
            heappush(heap,  -num)
            
        ans = 0 
        
        ith = 0 
        
        for _ in range(k):
            tmp = -heappop(heap) - ith
            
            if tmp <= 0: 
                break 
                
            ith += 1
            
            ans += tmp 
            
        return ans 
        
