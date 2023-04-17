# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def helper(start, end):            
            if start == end: 
                return (arr[start], 0)
            
            else: 
                minimum = inf 
                
                elem = 0 
                
                for i in range(start, end):
                    (left, leftSum) = helper(start, i)
                    (right, rightSum) = helper(i + 1, end)
                    
                    elem = max(elem, left, right)
                    
                    minimum = min(minimum, leftSum + rightSum + left*right)
                    
                return (elem, minimum)
            
        n = len(arr)
        
        return helper(0, n - 1)[1]
