# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1, dic2, ans = {}, {}, []
        for num in nums1: 
            dic1[num] = dic1.get(num, 0) + 1
        for num in nums2: 
            if num in dic1: 
                dic2[num] = dic2.get(num, 0) + 1
                if dic2[num] <= dic1[num]:
                    ans.append(num)
        return ans
        
        
