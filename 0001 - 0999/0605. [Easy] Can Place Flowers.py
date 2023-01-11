# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        first = True 
        
        count = 0 
        
        ans = 0 
        
        for flower in flowerbed: 
            if flower == 0: 
                count += 1 
                
            else: 
                if first: 
                    ans += count//2
                    first = False 
                else: 
                    ans += (count - 1)//2
                    
                count = 0 
        
        if first: 
            ans = (count + 1)//2
        else: 
            ans += count//2
        
        return ans >= n
                
