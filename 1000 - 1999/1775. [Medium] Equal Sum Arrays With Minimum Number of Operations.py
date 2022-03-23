# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        if 6*m < n or 6*n < m: 
            return -1 
        
        if sum(nums1) < sum(nums2):
            nums1, nums2 = nums2, nums1
            
        sum1, sum2 = sum(nums1), sum(nums2)
        
        nums1 = [-num for num in nums1]
        heapify(nums1)
        heapify(nums2)
        
        ans = 0
        
        while sum1 > sum2: 
            num1, num2 = nums1[0], nums2[0]
            if -1 - num1 > 6 - num2:
                sum1 += num1 + 1
                heapreplace(nums1, -1)
            else: 
                sum2 += 6 - num2
                heapreplace(nums2, 6)
            
            ans += 1
            
        return ans 
        

