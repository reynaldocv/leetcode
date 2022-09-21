# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m + n - 1, n - 1, -1):
            nums1[i] = nums1[i - n]
            
        i, j = n, 0 
        
        idx = 0 
        
        while i < m + n or j < n:
            val1 = nums1[i] if i < m + n else inf 
            val2 = nums2[j] if j < n else inf 
            
            if val1 < val2: 
                nums1[idx] = val1
                i += 1 
            else: 
                nums1[idx] = val2
                j += 1 
                
            idx += 1 
