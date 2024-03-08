# https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = set([])
        cols = set([])
        
        ans = 0 
        
        for (_type, index, value) in queries[:: -1]:
            if _type == 0: 
                if index not in rows: 
                    ans += value*(n - len(cols))
                    
                    rows.add(index)
                    
            else: 
                if index not in cols: 
                    ans += value*(n - len(rows))
                    
                    cols.add(index)
                    
        return ans 
                    
