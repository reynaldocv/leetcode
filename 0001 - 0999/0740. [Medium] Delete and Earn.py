# https://leetcode.com/problems/delete-and-earn/
    
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:        
        limit = 0 
        
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
            limit = max(limit, num)
            
        dp = [0 for _ in range(limit + 1)]
        
        ans = 0 
        
        for num in range(limit + 1):
            val3 = dp[num - 3] if num - 3 >= 0 else 0  
            val2 = dp[num - 2] if num - 2 >= 0 else 0 
            
            dp[num] += max(val3, val2) + num*counter[num]
            
            ans = max(ans, dp[num])
            
        return ans 
                        
            
        
        
        

        
            
        
