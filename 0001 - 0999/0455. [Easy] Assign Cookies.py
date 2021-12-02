# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n , m = len(g), len(s)
        g.sort(reverse = True)
        s.sort(reverse = True)
        i, j = 0, 0
        ans = 0
        while i < n and j < m: 
            if g[i] > s[j]:
                i += 1
            else:
                ans += 1
                j += 1
                i += 1
           
        return ans
        
        
