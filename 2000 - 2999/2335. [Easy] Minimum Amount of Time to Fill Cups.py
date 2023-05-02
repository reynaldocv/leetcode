# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0 
        
        heap = []
        
        for num in amount: 
            heappush(heap, -num)
            
        while heap[0] != 0: 
            num1 = heappop(heap) 
            num2 = heappop(heap) 
            
            if num1 < 0: 
                num1 += 1 
                
            if num2 < 0: 
                num2 += 1 
            
            heappush(heap, num1)                
            heappush(heap, num2)
            
            ans += 1 
            
        return ans 
                
