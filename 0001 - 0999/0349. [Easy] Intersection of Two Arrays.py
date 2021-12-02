# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set([])
        for i in nums1: 
            if i in nums2:
                ans.add(i)
        return ans
        
