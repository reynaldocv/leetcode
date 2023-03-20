# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        
        ans = 0 
        
        for flower in [0] + flowerbed + [0, 1]: 
            if flower == 0: 
                count += 1 
                
            else: 
                ans += (count - 1)//2
                    
                count = 0 
        
        return ans >= n
                
