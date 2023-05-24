# https://leetcode.com/problems/maximum-subsequence-score/

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        
        nums = [(nums2[i], nums1[i]) for i in range(n)]
        nums.sort(key = lambda item: (-item[0], -item[1]))
        
        arr = []  
        
        ans = -inf        
        tmp = 0
        
        for i in range(n):
            (minElem, num) = nums[i]            
            aSum = num + tmp
            
            idx = bisect_left(arr, num)
            
            if len(arr) >= k - 1:                
                ans = max(ans, minElem*aSum)
                
                if idx != 0: 
                    tmp += num - arr.pop(0)                    
                    insort(arr, num)
                    
            else: 
                tmp += num                  
                insort(arr, num)
            
        return ans 
        
        
        
