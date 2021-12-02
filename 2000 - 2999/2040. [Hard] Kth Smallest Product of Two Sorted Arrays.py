# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helper(val):
            ans = 0
            
            start, end = 0, len(nums2) - 1
            arr = neg[::-1] + pos if val >= 0 else neg + pos[::-1]
            
            for x in arr: 
                if x < 0: 
                    while start < len(nums2) and x*nums2[start] > val: 
                        start += 1
                    ans += len(nums2) - start
                elif x == 0: 
                    if 0 <= val: 
                        ans += len(nums2)
                else: 
                    while 0 <= end and x*nums2[end] > val: 
                        end -= 1
                    ans += end + 1
            
            return ans 
        
        neg = [x for x in nums1 if x < 0]
        pos = [x for x in nums1 if x >= 0]
        
        start, end = -10**10, 10**10 + 1
        while end - start > 0: 
            mid = (start + end) >> 1 
            if helper(mid) < k: 
                start = mid + 1
            else: 
                end = mid
        
        return start
    
