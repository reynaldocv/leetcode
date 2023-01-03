# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0 
        
        m, n = len(strs), len(strs[0])
        
        for i in range(n):
            go = False
            for j in range(1, m):
                if strs[j][i] < strs[j - 1][i]:
                    go = True
                    break 
                    
            if go: 
                ans += 1 
                    
        return ans 
                
            
            
