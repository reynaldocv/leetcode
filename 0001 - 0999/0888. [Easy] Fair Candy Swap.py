# https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        totalAlice = sum(aliceSizes)
        totalBob = sum(bobSizes)
        
        mid = (totalAlice + totalBob)//2
        
        seen = set()
        
        for num in aliceSizes: 
            seen.add(num) 
            
        for num in bobSizes: 
            tmp = mid - (totalBob - num)
            
            if tmp in seen: 
                return [tmp, num]
