# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ans = inf
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                tmp = 0 
                
                for num in nums[i: j]:
                    tmp = tmp | num 
                    
                if tmp >= k: 
                    ans = min(ans, j - i)
                    
        return -1 if ans == inf else ans 
        
