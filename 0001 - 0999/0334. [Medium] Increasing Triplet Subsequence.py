# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        
        right = [num for num in nums]
        
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1])
            
        left = nums[0]
        
        for i in range(1, n - 1):
            if left < nums[i] < right[i + 1]:
                return True 
            
            left = min(left, nums[i])
        
        return False 

class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = []
        
        for num in nums: 
            idx = bisect_left(arr, num)
            
            if idx < len(arr):
                arr[idx] = num 
            else: 
                arr.append(num)
                
        return len(arr) >= 3
    
        
