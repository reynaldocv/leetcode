# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        
        seen = defaultdict(lambda: defaultdict(lambda: 0))
        
        for word in arr: 
            m = len(word)
            
            visited = set()
            
            for width in range(1, m + 1):
                for i in range(0, m - width + 1):
                    tmp = word[i: i + width]
                    
                    if tmp not in visited:                     
                        seen[width][tmp] += 1 
                        
                        visited.add(tmp)
                    
        ans = ["" for _ in range(n)]
        
        for (ith, word) in enumerate(arr): 
            m = len(word)
            
            found = False 
            
            for width in range(1, m + 1):
                for i in range(0, m - width + 1):
                    tmp = word[i: i + width]
                    
                    if seen[width][tmp] == 1:
                        if ans[ith] == "":
                            ans[ith] = tmp
                            
                        else:
                            ans[ith] = min(ans[ith], tmp)
                        
                        found = True
                        
                if found: 
                    break 
                    
        return ans 
            
            
                
        
