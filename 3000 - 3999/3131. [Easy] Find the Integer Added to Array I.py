# https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        minElem1 = min(nums1)
        minElem2 = min(nums2)
        
        return minElem2 - minElem1
    
