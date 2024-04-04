# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @cache 
        def helper(prev1, prev2, idx):
            if idx == n: 
                return 0 
            
            else: 
                ans = inf 
                
                if prev1 < nums1[idx] and prev2 < nums2[idx]:
                    ans = min(ans, helper(nums1[idx], nums2[idx], idx + 1))
                    
                if prev2 < nums1[idx] and prev1 < nums2[idx]: 
                    ans = min(ans, 1 + helper(nums2[idx], nums1[idx], idx + 1))
                    
                return ans 
        
        n = len(nums1)
        
        return helper(-inf, -inf, 0)
        
