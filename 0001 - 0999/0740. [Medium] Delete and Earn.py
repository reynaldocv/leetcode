# https://leetcode.com/problems/delete-and-earn/
    
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        limit = max(nums)
        
        counter = defaultdict(lambda: 0)
        
        dp = defaultdict(lambda: 0)
        
        ans = 0 
        
        for num in nums: 
            counter[num] += 1 
        
        for i in range(1, limit + 1):
            dp[i] = i*counter[i] + max(dp[i - 2], dp[i - 3])
            
            ans = max(ans, dp[i])
            
        return ans 
            
                        
            
        
        
        

        
            
        
