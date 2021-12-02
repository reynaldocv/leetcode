# https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attackers = defaultdict(lambda: inf)
        (r, s) = king 
        for (x, y) in queens: 
            i, j = x - r, y - s
            if i == 0 or j == 0: 
                dist = abs(i + j)
                i = i//abs(i) if i != 0 else 0 
                j = j//abs(j) if j != 0 else 0
                attackers[(i, j)] = min(attackers[(i, j)], dist)
            if abs(i) == abs(j):
                dist = abs(i)
                i = i//abs(i) if i != 0 else 0 
                j = j//abs(j) if j != 0 else 0
                attackers[(i, j)] = min(attackers[(i, j)], dist)
                
        ans = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if attackers[(i, j)] != inf: 
                    dist = attackers[(i, j)]
                    ans.append((i*dist + r, j*dist + s))
                    
        return ans
