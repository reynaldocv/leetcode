# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0 
        n, m = len(nums1), len(nums2)
        arr = []
        
        for i in range(max(n, m) - 1, -1, -1):
            if i < m: 
                arr.append(nums2[i])
            if i < n and arr: 
                idx = bisect_left(arr, nums1[i])
                if idx != len(arr):
                    ans = max(ans, len(arr) - idx - 1)
                
        return ans
                
