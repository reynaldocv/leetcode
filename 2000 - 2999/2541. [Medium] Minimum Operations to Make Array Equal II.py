# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        
        if k == 0:
            if nums1 == nums2: 
                return 0 
            
            else: 
                return -1 
        
        if sum(nums1) != sum(nums2):
            return -1
        
        modifcations = 0 
        
        for i in range(n):
            num1 = nums1[i]
            num2 = nums2[i]
            
            diff = abs(num1 - num2)
            
            if diff % k == 0: 
                modifcations += (diff//k)
                
            else: 
                return -1 
            
        if modifcations % 2 == 1: 
            ans = -1 
        
        else:         
            ans = modifcations//2
            
        return ans 
        
