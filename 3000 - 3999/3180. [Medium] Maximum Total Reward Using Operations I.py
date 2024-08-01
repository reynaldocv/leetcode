# https://leetcode.com/problems/maximum-total-reward-using-operations-i/

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        @cache
        def helper(val, idx):
            if idx >= n: 
                return val
            
            else: 
                ans = helper(val, idx + 1)
                
                if val < rewardValues[idx]:
                    tmp = val + rewardValues[idx]
                    
                    ans = max(ans, helper(tmp, idx + 1))
                        
                return ans 
            
        rewardValues = sorted(set(rewardValues))
        
        n = len(rewardValues)
        
        return helper(0, 0)
                    
                
