# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        ans = 0
        for pile in piles: 
            heappush(heap, -pile)
            ans += pile
     
        for i in range(k):     
            quantity = heappop(heap)
            newQuantity = quantity//2
            ans += quantity - newQuantity        
            if newQuantity != -1: 
                heappush(heap, newQuantity)                
            else: 
                break
                
        return ans
            
            
