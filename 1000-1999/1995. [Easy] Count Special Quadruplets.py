# https://leetcode.com/problems/count-special-quadruplets/

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0         
        n = len(nums)
        for i, j, k , l in combinations(range(n), 4):
            i, j, k, l = sorted([i, j, k, l])
            if nums[i] + nums[j] + nums[k] == nums[l]:
                ans += 1
        
        return ans
                
        
        
