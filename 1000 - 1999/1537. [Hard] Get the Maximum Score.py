# https://leetcode.com/problems/get-the-maximum-score/

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        seen1 = {num: True for num in nums1}
        seen2 = {num: True for num in nums2}
        
        seen = {num: True for num in seen1 if num in seen2}
                
        n, m = len(nums1) ,len(nums2)
        sum1, sum2 = 0, 0
        
        i, j = 0, 0 
        
        for _ in range(len(seen) + 1):
            while i < n and nums1[i] not in seen: 
                sum1 += nums1[i]
                i += 1 
            
            while j < m and nums2[j] not in seen:
                sum2 += nums2[j]
                j += 1 
            
            if i < n and j < m: 
                sum1 = sum2 = (nums1[i] + max(sum1, sum2)) % MOD
                i, j = i + 1, j + 1
                
        return max(sum1, sum2) % MOD
            
        
            
        
        
