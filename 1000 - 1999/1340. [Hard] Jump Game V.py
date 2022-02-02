# https://leetcode.com/problems/jump-game-v/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @cache
        def helper(i):
            ans = 0            
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] <= arr[j]: 
                    break
                    
                ans = max(ans, helper(j))
                
            for j in range(i - 1, max(0, i - d) -1, -1):                
                if arr[i] <= arr[j]: 
                    break 
                
                ans = max(ans, helper(j))
                
            return ans + 1
        
        n = len(arr)
    
        return max(helper(i) for i in range(n))
