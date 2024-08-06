# https://leetcode.com/problems/alternating-groups-ii/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        
        idx = None
        
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                idx = i + 1
                
                break
                
        if idx == None: 
            if colors[0] != colors[-1]:
                return n 
            
            else: 
                return max(n - k + 1, 0)            
        
        colors = colors[idx: ] + colors[: idx]
        
        prev = 0 
        cnt = 0

        ans = 0 
        
        for color in colors + [colors[-1]]: 
            if color != prev: 
                cnt += 1

            else: 
                if cnt >= k: 
                    ans += (cnt - k + 1)

                cnt = 1 

            prev = color 

        return ans 

                    
            
    
        
        
                
        
