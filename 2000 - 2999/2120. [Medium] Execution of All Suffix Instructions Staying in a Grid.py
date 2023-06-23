# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        
        moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        
        ans = []
        
        for i in range(m):            
            (x, y) = startPos
            
            counter = 0 
                
            for move in s[i: ]:
                x, y = x + moves[move][0], y + moves[move][1]

                if 0 <= x < n and 0 <= y < n: 
                    counter += 1 

                else: 
                    break 

            ans.append(counter)

        return ans 
