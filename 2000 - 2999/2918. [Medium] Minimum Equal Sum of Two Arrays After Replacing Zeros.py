# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, cnt1 = sum(nums1), sum(1 for num in nums1 if num == 0)
        sum2, cnt2 = sum(nums2), sum(1 for num in nums2 if num == 0)
        
        sum1 += cnt1 
        sum2 += cnt2 
        
        if sum1 == sum2: 
            return sum1 
        
        elif sum1 > sum2: 
            if cnt2 > 0: 
                return sum1 
            
        else: 
            if cnt1 > 0: 
                return sum2 
            
        return -1 
