# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:        
        nums = [(num, i) for (i, num) in enumerate(nums)]
        nums.sort(reverse = True)
        
        nums = nums[:k]
        nums.sort(key = lambda item: item[1])
        
        return [num for (num, _) in nums]
        
        
  
                
                
        
            
        
