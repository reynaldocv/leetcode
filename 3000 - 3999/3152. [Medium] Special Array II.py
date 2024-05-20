# https://leetcode.com/problems/special-array-ii/

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prev = (nums[0] % 2) + 1        
        cnt = 0
        
        dp = []
        
        for num in nums: 
            if num % 2 == prev % 2: 
                cnt += 1 
                
            prev = num
            
            dp.append(cnt)
            
        ans = []     
        
        for (start, end) in queries: 
            ans.append(dp[start] == dp[end])
            
        return ans 
            
            
