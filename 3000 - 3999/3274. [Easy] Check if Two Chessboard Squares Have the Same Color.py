# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        value = {chr(ord("a") + i): i + 1 for i in range(8)}
        
        (x1, y1) = (value[coordinate1[0]], int(coordinate1[1]))
        
        (x2, y2) = (value[coordinate2[0]], int(coordinate2[1]))
        
        return (x1 + y1) % 2 == (x2 + y2) % 2
        
