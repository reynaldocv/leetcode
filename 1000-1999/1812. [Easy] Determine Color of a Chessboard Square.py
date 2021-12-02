# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = "abcdefgh"
        values = {}
        for letter in letters: 
            values[letter] = ord(letter) % 2
        
        return (values[coordinates[0]] + int(coordinates[1]))%2 == 1
        
