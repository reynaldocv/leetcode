# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        arr = []
        
        ans = [0 for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            num = nums[i]
            
            idx = bisect_left(arr, num)
            
            ans[i] = idx
            
            arr.insert(idx, num)
            
        return ans 
        
