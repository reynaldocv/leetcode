# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def helper(u): 
            nonlocal ans 
            arr = [0, 0]
            for v in tree[u]: 
                val = helper(v)                
                if s[u] != s[v]: 
                    insort(arr, val)
                    arr = arr[-2: ]
                        
            ans = max(ans, sum(arr) + 1)
            
            return 1 + arr[1]
        
        tree = [[] for _ in parent]
        
        for (i, father) in enumerate(parent): 
            if father != -1: 
                tree[father].append(i)
        
        ans = 0
        
        helper(0)
        
        return ans
