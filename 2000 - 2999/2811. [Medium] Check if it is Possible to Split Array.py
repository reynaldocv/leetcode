# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        @cache 
        def helper(start, end):
            if start == end: 
                return True 
            
            else: 
                for i in range(start, end):
                    if helper(start, i) and helper(i + 1, end):
                        if sum(nums[start: end + 1]) >= m: 
                            return True 
                        
                return False 
            
        n = len(nums)
        
        if n <= 2: 
            return True 
        
        return helper(0, n - 1)
