# https://leetcode.com/problems/beautiful-towers-ii/

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:        
        def helper(arr):
            stack = [(0, -1)]
            
            ans = [0]
            
            for (i, num) in enumerate(arr): 
                while stack and stack[-1][0] > num: 
                    stack.pop()
                    
                start = stack[-1][1]
                tmp = ans[start + 1] + (i - start)*num
                
                ans.append(tmp)                
                stack.append((num, i))
                
            return ans 
        
        n = len(maxHeights)
        
        left = helper(maxHeights)
        right = helper(maxHeights[:: -1])[:: -1]
        
        ans = 0
        
        for i in range(n):
            ans = max(ans, left[i] + right[i])
            
        return ans 
                    
