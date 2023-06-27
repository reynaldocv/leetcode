# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def helper(son):
            while parent[son] != son: 
                son = parent[son]
                
            return son
        
        n = len(s1)
        
        index = {chr(ord("a") + i): i for i in range(26)}
        
        parent = [i for i in range(26)]
        
        for i in range(n):
            idx1 = index[s1[i]]
            idx2 = index[s2[i]]
            
            parent1 = helper(idx1)
            parent2 = helper(idx2)
            
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        ans = ""
        
        for char in baseStr: 
            idx = index[char]
            
            ans += chr(ord("a") + helper(idx))

        return ans 
