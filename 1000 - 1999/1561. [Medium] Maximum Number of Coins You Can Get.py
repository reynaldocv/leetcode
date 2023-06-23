# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        
        piles.sort() 
        
        ans = 0 
        
        for _ in range(n//3):
            piles.pop()
            
            ans += piles.pop() 
            
            piles.pop(0)
            
        return ans 
        
