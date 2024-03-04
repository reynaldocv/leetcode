# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/submissions/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1 = [nums[0]]
        nums2 = [nums[1]]
        
        for num in nums[2: ]:
            if nums1[-1] >= nums2[-1]:
                nums1.append(num)
                
            else: 
                nums2.append(num)
                
        return nums1 + nums2
        
