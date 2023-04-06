# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        def helper(arr):
            prev = 0 
            
            ans = [0]
            
            for num in arr[: -1]: 
                ans.append(ans[-1] + num)
                
            return ans 
        
        n = len(nums)
        
        left = helper(nums)
        right = helper(nums[:: -1])[:: -1]
        
        ans = []
        
        for i in range(n):
            ans.append(abs(left[i] - right[i]))
            
        return ans 
