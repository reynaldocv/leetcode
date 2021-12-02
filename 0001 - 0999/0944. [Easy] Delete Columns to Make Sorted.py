# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        arr = [[strs[i][j] for i in range(n)] for j in range(m)]
        
        print(arr)
        ans = 0
        for i in range(m):
            go = False
            for j in range(1, n):
                if ord(arr[i][j - 1]) > ord(arr[i][j]):
                    go = True
                    break 
                    
            if go: 
                ans += 1
        
        return ans
