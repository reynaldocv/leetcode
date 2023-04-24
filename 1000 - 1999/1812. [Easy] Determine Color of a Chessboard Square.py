# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        color = False 
        
        if int(coordinates[1]) % 2 == 0:
            color = not color
            
        if coordinates[0] in "bdfh":
            color = not color
            
        return color
            
