# https://leetcode.com/problems/uncrossed-lines/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:        
        @cache
        def helper(i, j):
            
            if i >= n or j >= m: 
                return 0 
            else: 
                num = nums1[i]
                if num in nums2[j:]:
                    j2 = j + nums2[j:].index(num)
                    val1 = 1 + helper(i + 1, j2 + 1)
                    val2 = helper(i + 1, j)
                
                    return max(val1, val2)
                
                else: 
                    return helper(i + 1, j)
                
        n, m = len(nums1), len(nums2)    
        
        return helper(0, 0)
        
      
        
