# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        aux = []
        ans = []
        for r in range(R):
            for c in range(C):
                dist = abs(r0 - r) + abs(c - c0)
                aux.append((dist, (r, c)))
        aux.sort()
        for (dis, pair) in aux:
            ans.append(pair)
        return ans
        
                
