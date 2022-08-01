# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums: 
            if num != 0: 
                seen.add(num)
                
        return len(seen)
        
