# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        nums.sort() 
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            if num <= target//2: 
                idx = bisect_left(nums, target - num + 1)   
                idx -= 1 

                ans += 2**(idx - i)
                ans %= MOD
                
            else: 
                break
                    
        return ans 
    
        
