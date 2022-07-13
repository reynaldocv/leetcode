# https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        def helper(value):
            ans = 0 
            
            for num in arr: 
                if num > value:
                    ans += num - value
                    
            return ans 
            
        n = len(nums1)
        arr = []
        
        for i in range(n):
            arr.append(abs(nums1[i] - nums2[i]))
            
        start = -1 
        end = max(arr)
        
        while end - start > 1: 
            mid = (end + start)//2 
            
            if helper(mid) <= k1 + k2:
                end = mid 
            else: 
                start = mid 
        
        if end == 0: 
            return 0 
        
        ans = 0 
        if helper(end) == k1 + k2: 
            for num in arr: 
                ans += (end)**2 if num > end else num**2
            
        else:
            for num in arr: 
                ans += (start)**2 if num > start else num**2
            
            diff = helper(start) - k1 - k2
            ans += diff*(end**2) - diff*(start**2)
                                
        return ans 
