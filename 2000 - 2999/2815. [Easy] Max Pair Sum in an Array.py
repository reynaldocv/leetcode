# https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def helper(num):
            ans = 0 
            
            while num > 0: 
                unit = num % 10
                ans = max(ans, unit)
                
                num //= 10 
                
            return ans 
        
        seen = defaultdict(lambda: [])
        
        for num in nums: 
            seen[helper(num)].append(num)
            
        ans = -1
        
        for key in seen:
            n = len(seen[key])
            
            if n >= 2: 
                seen[key].sort()
                
                ans = max(ans, seen[key][-1] + seen[key][-2])
                
        return ans
        
