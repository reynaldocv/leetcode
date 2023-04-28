# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        seen = set() 
        
        counter = 0 
        
        for num in nums: 
            if num in seen: 
                seen.remove(num)
                counter += 1 
                
            else: 
                seen.add(num)
                
        return [counter, len(seen)]
                
        
            
