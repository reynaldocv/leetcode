# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        aux = []
        for i in range(n):
            s = sum(mat[i])
            aux.append((s, i))
        aux.sort()
        ans = []
        for (a, b) in aux:
            ans.append(b)
        
            
        return ans[0:k]
        
