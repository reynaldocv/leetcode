# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        post = [False for _ in range(n)]
        post[-1] = True
        
        prev = [False for _ in range(n)]
        prev[0] = True
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                post[i] = True
            else: 
                break
                
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                prev[i] = True
            else: 
                break
        
        for i in range(n):
            _prev = prev[i - 1] if i > 0 else True
            _post = post[i + 1] if i < n - 1 else True
            _prevNum = nums[i - 1] if i > 0 else -inf
            _postNum = nums[i + 1] if i < n - 1 else inf
            if _prev and _post and _prevNum <= _postNum: 
                return True
        
        return False
            
