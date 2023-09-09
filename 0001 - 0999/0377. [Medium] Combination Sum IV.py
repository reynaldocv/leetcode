# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(number):
            if number == 0: 
                return 1 
            
            elif number > 0: 
                ans = 0
                
                for num in nums: 
                    ans += helper(number - num)
                    
                return ans 
            
            return 0
        
        nums = {num for num in nums}
        
        return helper(target)        

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        
        for i in range(1, target + 1):
            for num in nums: 
                if num <= i: 
                    dp[i] += dp[i - num]
                    
        return dp[-1]
       
        
        
