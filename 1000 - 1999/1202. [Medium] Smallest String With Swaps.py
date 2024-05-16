# https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def helper(son):
            while son != parent[son]:
                son = parent[son]
                
            return son
        
        n = len(s)
        
        parent = [i for i in range(n)]
        
        for (u, v) in pairs: 
            parentU = helper(u)
            parentV = helper(v)
            
            parent[parentU] = parent[parentV] = min(parentU, parentV)
        
        letters = defaultdict(lambda: [])
        
        for (i, char) in enumerate(s):
            parentI = helper(i)
            
            letters[parentI].append(char)
            
        for key in letters: 
            letters[key].sort() 
            
        ans = ""
        
        for i in range(n):
            parentI = helper(i)
            
            ans += letters[parentI].pop(0)
            
        return ans 
