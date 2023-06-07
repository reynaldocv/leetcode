# https://leetcode.com/problems/maximum-or/

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        def helper(arr):
            ans = [arr[0]]
            
            for num in arr[1: ]: 
                ans.append(ans[-1] | num)
                
            return ans 
        
        n = len(nums)
        
        left = helper(nums)
        right = helper(nums[:: -1])[:: -1]
        
        ans = 0 
        
        for i in range(n):
            l = left[i - 1] if i - 1 >= 0 else 0 
            r = right[i + 1] if i + 1 < n else 0 
            
            ans = max(ans, l | r | nums[i] << k)
            
        return ans 
