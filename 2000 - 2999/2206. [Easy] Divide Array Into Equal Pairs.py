# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums: 
            if num in seen: 
                seen.remove(num)
                
            else: 
                seen.add(num)
                
        return len(seen) == 0
            
            
