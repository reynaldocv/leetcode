# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [inf for i in range(n)]
        arr[0] = 1
        for i in range(n - 1):
            if arr[i] != inf:
                for j in range(i + 1, i + nums[i] + 1):
                    if j < n:
                        arr[j] = min(arr[i] + 1, arr[j])                
            
        return arr[n - 1] - 1
        
        
        
