# https://leetcode.com/problems/zuma-game/

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @cache
        def clean(board):
            stack = []
            
            for char in board: 
                if stack and stack[-1][0] != char and stack[-1][1] >= 3: 
                    stack.pop()
                if not stack or stack[-1][0] != char:
                    stack.append([char, 1])
                else: 
                    stack[-1][1] += 1
                
            if stack and stack[-1][1] >= 3: 
                stack.pop()
                
            return "".join([a*b for (a, b) in stack])
        
        @cache
        def dfs(board, hand):
            if not board: 
                return 0 
            
            if not hand: 
                return inf
            
            n = len(board)
            ans = inf
            
            for (i, char) in enumerate(hand):
                newHand = hand[:i] + hand[i + 1:]
                for j in range(n + 1):
                    newBoard = clean(board[:j] + char + board[j:])
                    ans = min(ans, 1 + dfs(newBoard, newHand))
            
            return ans
        
        ans = dfs(board, hand)
        
        return -1 if ans == inf else ans
