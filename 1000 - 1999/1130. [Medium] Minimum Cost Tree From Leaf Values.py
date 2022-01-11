# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def helper(start, end):
            if start == end: 
                return (0, arr[start])
            elif start + 1 == end: 
                return (arr[start]*arr[end], max(arr[start], arr[end]))
            else: 
                ans = (inf, inf)
                for i in range(start, end):
                    left, maxL = helper(start, i)
                    right, maxR = helper(i + 1, end)
                    
                    ans = min(ans, (left + right + maxL*maxR, max(maxL, maxR)))
                    
                return ans
                
        n = len(arr)
        
        return helper(0, n - 1)[0]
