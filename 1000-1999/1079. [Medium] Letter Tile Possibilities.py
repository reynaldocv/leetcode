# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        elems = [tile for tile in tiles]
        
        for i in range(1, len(tiles) + 1):
            arr = set(permutations(elems, i))
            ans += len(arr)
        
        return ans
        
        
