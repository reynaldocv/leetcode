# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def firstMax(array, val):
            ans = -1
            for i in range(len(array)):
                if array[i] > val:
                    ans = array[i]
                    break
            return ans
        
        ans = []
        n = len(nums1)
        for i in range(n):
            ind = nums2.index(nums1[i])
            ans.append(firstMax(nums2[ind + 1:], nums1[i]))
        
        return ans
        
