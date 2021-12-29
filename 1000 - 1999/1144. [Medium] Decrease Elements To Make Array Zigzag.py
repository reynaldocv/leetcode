# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            ans = 0
            for i in range(1, n, 2):
                right = arr[i + 1] if i + 1 < n else inf
                num = arr[i]
                if arr[i - 1] > num and num < right: 
                    continue
                else: 
                    ans += num - (min(arr[i - 1], right)) + 1
                
            return ans
        
        n = len(nums)
        
        ans = helper(nums)
        nums.insert(0, inf)
        
        return min(ans, helper(nums))
        
        
        
        
