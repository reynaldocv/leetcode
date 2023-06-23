# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        greater = []        
        equals = []
        
        for num in nums: 
            if num < pivot: 
                lower.append(num)
                
            elif num > pivot: 
                greater.append(num)
                
            else: 
                equals.append(num)
                
        return lower + equals + greater
        
        
            
        

