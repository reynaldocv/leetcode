# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen1 = {num: True for num in nums1}
        seen2 = {num: True for num in nums2}
        
        ans = [[], []]
        
        seen = {}
        for num in nums1: 
            if num not in seen: 
                seen[num] = True
                if num not in nums2: 
                    ans[0].append(num)

        seen = {}
        for num in nums2:             
            if num not in seen: 
                seen[num] = True        
                if num not in nums1: 
                    ans[1].append(num)
                
        return ans 
