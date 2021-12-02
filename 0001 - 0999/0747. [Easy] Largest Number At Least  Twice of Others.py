# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)        
        if n <= 1: return 0
        
        max_ = 0
        ans = -1
        for i in range(n): 
            if max_ < nums[i]:
                max_ = nums[i]
                ans = i
                
        go = True       
        for i in range(n):
            if nums[i] != max_:
                if nums[i]*2 > max_:
                    go = False
                    break
            
        return ans if go else -1
