# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:        
        n = len(colsum)
        ans = [[0 for _ in range(n)] for _ in range(2)]
        
        for (i, num) in enumerate(colsum): 
            if num == 2: 
                upper -= 1
                lower -= 1
                ans[0][i] = ans[1][i] = 1
            elif num == 1: 
                if upper > lower: 
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1
                    
        if upper == 0 and lower == 0: 
            return ans
        else:
            return []
                    
