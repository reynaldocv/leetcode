# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if 1 not in nums: return True
        idx = nums.index(1)
        ans, n, l = True, len(nums), 0
        for i in range(idx + 1, n):
            if nums[i] == 0: 
                l += 1                
            else: 
                if (l < k):
                    ans = False
                    break
                l = 0
        return ans


                
        
