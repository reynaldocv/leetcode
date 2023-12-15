# https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums1)
        
        arr = []
        
        aSum = 0 
        
        for i in range(n):
            aSum  += abs(nums1[i] - nums2[i])
            
            arr.append(nums1[i])
            
        arr.sort() 
        
        ans = inf 
        
        for i in range(n):
            tmp = abs(nums1[i] - nums2[i])
            
            num = nums2[i]
            
            idx = bisect_left(arr, num)
            
            if idx < n: 
                ans = min(ans, aSum - tmp + abs(arr[idx] - num))
                
            if idx - 1 >= 0:
                ans = min(ans, aSum - tmp + abs(arr[idx - 1] - num))
                
        return ans % MOD
            
        
