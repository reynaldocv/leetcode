# https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def helper(start, end, turn):
            if start == end: 
                return turn*nums[start]
            else: 
                val1 = turn*nums[start] + helper(start + 1, end, -turn)
                val2 = turn*nums[end] + helper(start, end - 1, - turn)
                
                return max(val1, val2) if turn == 1 else min(val1, val2)
                
        n = len(nums)
        return helper(0, n - 1, 1) >= 0
