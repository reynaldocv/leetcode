# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        seen = {start: True}
        
        while stack: 
            x = stack.pop()
            if arr[x] == 0: 
                return True
            for y in [x + arr[x], x - arr[x]]:
                if 0 <= y < n: 
                    if y not in seen: 
                        seen[y] = True
                        stack.append(y)
                        
        return False
                    
            
        
