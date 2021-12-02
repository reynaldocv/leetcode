# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        ans = []
        idx = [0 for i in range(n)] 
        while len(ans) < k: 
            arr = [[matrix[i][idx[i]], i] if (idx[i] < n) else [inf, i] for i in range(n)]
            val, position = min(arr)
            if val == inf: 
                break
            ans.append(val)
            idx[position] += 1
        
        return ans[min(k - 1, len(ans) - 1)]
            
