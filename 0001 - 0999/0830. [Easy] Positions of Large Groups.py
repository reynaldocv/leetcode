# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev = "$"
        
        ans = []
        
        start = -1
        
        for (i, char) in enumerate(s + "$"):
            if prev != char:
                if i - start >= 3:
                    ans.append((start, i - 1))
                    
                start = i 
                prev = char
                
        return ans
                
