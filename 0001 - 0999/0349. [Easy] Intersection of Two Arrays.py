# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        
        for num in nums1: 
            seen.add(num)
            
        ans = set()
            
        for num in nums2: 
            if num in seen and num not in ans:
                ans.add(num)
        
        return ans 
        
