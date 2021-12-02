# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:        
        n = len(nums)
        left = [num for num in nums]
        
        for i in range(1, n):
            left[i] = min(left[i], left[i - 1])
            
        arr = [nums[-1]]
        
        for i in range(n - 2, 0, -1):
            if left[i - 1] < nums[i]:
                idx = bisect_right(arr, left[i - 1])
                if idx < len(arr):
                    if arr[idx] < nums[i]:
                        return True
            
            insort(arr, nums[i])
            
        return False
      
class Solution2:
    def find132pattern(self, nums: List[int]) -> bool: 
        stack = []
        ref = -inf
        
        for x in nums[::-1]:
            if x < ref: 
                return True
            while stack and stack[-1] < x: 
                ref = stack.pop()
            
            stack.append(x)
            
        return False

        
        

      
