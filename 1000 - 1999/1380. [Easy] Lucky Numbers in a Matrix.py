# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            aux = [(matrix[r][c], c) for c in range(col)]
            aux.sort()
            aux2 = [matrix[r_][aux[0][1]] for r_ in range(row)]
            aux2.sort(reverse = True)
            
            if aux[0][0] == aux2[0]:
                return [aux[0][0]]
