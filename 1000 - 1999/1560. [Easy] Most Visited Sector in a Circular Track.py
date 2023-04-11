# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        
        if start == end: 
            return [start]
        
        elif start <= end:
            return [i for i in range(start, end + 1)]
        
        else: 
            return [i for i in range(1, end + 1)] + [i for i in range(start, n + 1)]

            
        
        
