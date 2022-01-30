# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = {}
        for num in nums: 
            seen[num] = True
            
        while original in seen:
            original *= 2
            
        return original
        
