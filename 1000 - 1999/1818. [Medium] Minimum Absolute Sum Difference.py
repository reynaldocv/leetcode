# https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums1)
        aSum = 0 
        for i in range(n):
            aSum += abs(nums1[i] - nums2[i]) 
            
        ans = aSum
        sort1 = sorted(nums1)
        
        for i in range(n):
            idx = bisect_left(sort1, nums2[i])
            if idx <= n - 1 and sort1[idx] == nums2[i]:
                ans = min(ans, aSum - abs(nums1[i] - nums2[i]))
            
            else: 
                right = sort1[idx] if idx != n else inf
                left = sort1[idx - 1] if idx != 0 else -inf
                
                aux = min(abs(left - nums2[i]), abs(right - nums2[i]))
                
                ans = min(ans, aSum - abs(nums1[i] - nums2[i]) + aux)
            
        return ans % MOD
            
        
