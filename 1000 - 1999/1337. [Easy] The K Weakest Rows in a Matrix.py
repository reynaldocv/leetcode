# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        
        arr = [i for i in range(n)]
        
        arr.sort(key = lambda item: sum(mat[item]))
        
        return arr[: k]
