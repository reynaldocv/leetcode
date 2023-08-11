# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(nth):
            start = -10**6 - 1
            end = 10**6 + 1
            
            while end - start > 1: 
                middle = (end + start)//2
                
                if collaborator(middle) >= nth: 
                    end = middle 
                    
                else: 
                    start = middle 
                    
            return end 
        
        def collaborator(value):
            cnt1 = bisect_right(nums1, value)
            cnt2 = bisect_right(nums2, value)

            return cnt1 + cnt2
        
        m, n = len(nums1), len(nums2)
        
        if (m + n) % 2 == 1:   
            middle = (m + n)//2
            
            return helper(middle + 1)
        
        else: 
            left = (m + n)//2
            right = (m + n)//2 + 1
            
            return (helper(left) + helper(right))/2
