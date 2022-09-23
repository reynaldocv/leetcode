# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set()
        seen2 = set()
        
        for num in nums1: 
            seen1.add(num)
            
        for num in nums2: 
            seen2.add(num)
            
        ans = []
            
        for key in seen1: 
            if key in seen2: 
                ans.append(key)
                
        return ans 
        
