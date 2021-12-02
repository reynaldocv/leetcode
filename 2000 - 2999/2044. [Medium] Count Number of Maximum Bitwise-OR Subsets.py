# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def helper(prev, idx):
            if prev == bitwiseOR: 
                self.ans += 1
            for i in range(idx, n):
                helper(prev | nums[i], i + 1)
        
        self.ans = 0 
        n = len(nums)
        
        bitwiseOR = 0
        for num in nums: 
            bitwiseOR = bitwiseOR | num
        
        helper(0, 0)
        
        return self.ans
                
        
        
        
