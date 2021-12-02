# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def helper(cur, jump):
            if cur == end: 
                return True
            if cur > end: 
                return False
            
            for nextStep in [jump - 1, jump, jump + 1]:
                if nextStep > 0: 
                    if cur + nextStep in stones: 
                        if helper(cur + nextStep, nextStep):
                            return True

            return False
        
        end = stones[-1]        
        stones = {stone: True for stone in stones}
        
        if 1 not in stones: 
            return False
        
        return helper(1, 1)
