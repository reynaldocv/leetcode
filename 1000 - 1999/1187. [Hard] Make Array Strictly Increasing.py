# https://leetcode.com/problems/make-array-strictly-increasing/

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        @cache
        def helper(i, prev):
            if i == n: 
                return 0 
            else: 
                ans = inf
                if prev < arr1[i]:
                    ans = helper(i + 1, arr1[i])
                
                k = bisect_right(arr2, prev)
                if k < m:
                    ans = min(ans, 1 + helper(i + 1, arr2[k]))
                
                return ans
            
        n, m = len(arr1), len(arr2)
        arr2.sort()
        
        ans = helper(0, -inf)
        
        return ans if ans < inf else -1
    
