# https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        temp = []
        even = True
        for i in range(len(board)-1, -1, -1):
            if even:
                temp.extend(board[i])
            else:
                temp.extend(board[i][::-1])
            even = not even

        n = len(temp)
        target = n - 1
        
        stack = [(0, 0)]        
        seen = {}

        while stack:
            (x, ans) = stack.pop(0)            
            if x == target:
                return ans
            
            for y in range(x + 1, min(x + 7, n)):
                if y not in seen:
                    seen[y] = True 
                    if temp[y] == -1:
                        stack.append((y, ans + 1))
                    else:
                        stack.append((temp[y] - 1, ans + 1))

        return -1
