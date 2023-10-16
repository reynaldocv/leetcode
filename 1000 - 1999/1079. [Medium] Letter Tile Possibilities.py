# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(arr):
            ans.add("".join(arr))
            
            for i in range(n):
                if visited[i] == False: 
                    arr.append(tiles[i])
                    visited[i] = True

                    helper(arr)

                    visited[i] = False
                    arr.pop()

        n = len(tiles)
        
        visited = [False for _ in range(n)]
        
        ans = set()
        
        helper([])
        
        return len(ans) - 1

class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        elems = [tile for tile in tiles]
        
        for i in range(1, len(tiles) + 1):
            arr = set(permutations(elems, i))
            ans += len(arr)
        
        return ans
        
        
