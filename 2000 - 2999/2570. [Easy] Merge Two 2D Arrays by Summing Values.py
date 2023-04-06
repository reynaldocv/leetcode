# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        
        i = 0 
        
        j = 0 
        
        ans = []
        
        while i < m or j < n: 
            (idx1, num1) = nums1[i] if i < m else (inf, inf)
            (idx2, num2) = nums2[j] if j < n else (inf, inf)
            
            if idx1 == idx2: 
                ans.append((idx1, num1 + num2))
                
                i += 1 
                j += 1 
            
            elif idx1 < idx2: 
                ans.append((idx1, num1))
                i += 1 
                
            else: 
                ans.append((idx2, num2))
                j += 1 
                
        return ans 
            
