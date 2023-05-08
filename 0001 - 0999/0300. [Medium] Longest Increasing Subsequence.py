# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        
        for num in nums: 
            idx = bisect_left(arr, num)
            
            if idx == len(arr):
                arr.append(num)
                
            else: 
                arr[idx] = num 
                
        return len(arr)        
        

    

        
        
