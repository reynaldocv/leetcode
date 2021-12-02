# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = [0, 0]
        for i in position:
            counter[i % 2] += 1
        
        return min(counter)
