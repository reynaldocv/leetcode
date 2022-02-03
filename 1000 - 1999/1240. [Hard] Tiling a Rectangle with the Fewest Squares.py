# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        def helper(x): 
            nonlocal ans 
            if x < ans: 
                if min(heights) == n: 
                    ans = x
                else: 
                    height = min(heights)
                    i = heights.index(height)
                    j = 0 
                    
                    while i + j < m and height + j < n and  heights[i + j] == height: 
                        j += 1

                    for jj in range(j, 0, -1): 
                        for ii in range(i, i + jj): 
                            heights[ii] += jj
                            
                        helper(x + 1)
                        
                        for ii in range(i, i + jj): 
                            heights[ii] -= jj

        if n == m: 
            return 1        
        
        heights = [0 for _ in range(m)]
                            
        ans = max(n, m)        
        helper(0)
        
        return ans 

    
