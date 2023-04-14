# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        
        ref = -inf 
        
        for num in nums[:: -1]:
            if num < ref: 
                return True 
            
            while stack and stack[-1] < num: 
                ref = stack.pop() 
                
            stack.append(num)
        
        return False 
    

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        
        left = [num for num in nums]
        
        for i in range(1, n):
            left[i] = min(left[i], left[i - 1])
            
        arr = [nums[-1]]
        
        for i in range(n - 2, 0, -1):
            elem = left[i - 1]
            
            if elem < nums[i]:
                idx = bisect_left(arr, elem + 1)
                
                if idx < len(arr) and elem < arr[idx] < nums[i]:
                    return True 
                
            insort(arr, nums[i])
            
        return False         
        

      
