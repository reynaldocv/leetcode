# https://leetcode.com/problems/count-good-triplets-in-an-array/

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        index = {num: i for (i, num) in enumerate(nums1)}
        
        n = len(nums1)
        arr = []
        ans = 0 
        
        for num in nums2:
            idx = index[num]
            
            left = bisect_left(arr, idx)
            right = (n - 1 - idx) - (len(arr) - left)
            
            ans += left * right            
            insort(arr, idx)
        
        return ans
    
    
