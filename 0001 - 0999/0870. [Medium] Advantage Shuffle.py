# https://leetcode.com/problems/advantage-shuffle/

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        ans = []
        
        for num in nums2:
            idx = bisect_left(nums1, num + 1)
            if idx == len(nums1):
                num = nums1.pop(0)                
            else: 
                num = nums1.pop(idx)
                
            ans.append(num)
            
        return ans
        
