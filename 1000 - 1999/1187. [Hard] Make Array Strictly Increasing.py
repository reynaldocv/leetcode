# https://leetcode.com/problems/make-array-strictly-increasing/

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        @cache
        def helper(i, prev):
            if i == m: 
                return 0 
            
            else: 
                ans = inf 
                
                if arr1[i] > prev: 
                    ans = helper(1 + i, arr1[i])
                    
                idx = bisect_right(arr2, prev)
                
                if idx < n:
                    ans = min(ans, 1 + helper(i + 1, arr2[idx]))
                    
                return ans
            
        m, n = len(arr1), len(arr2)
        
        arr2.sort()
        
        ans =  helper(0, -1)
        
        return ans if ans < inf else -1
    
