# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums: 
            seen.add(num)
            
        arr = [num for num in seen]
        
        arr.sort(key = lambda item: -item)
        
        n = len(arr)
        
        return arr[2] if n > 2 else arr[0]
        
                
        
        
                
