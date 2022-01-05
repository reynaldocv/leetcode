# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def helper(i, node, p):
            if i == m:
                return node['$']*(1 - p)

            ans =  node['$']*(1 - p) if '$' in node else 0
            for char in node:
                if char != s[i] and p == 1 and char != '$':
                    ans += helper(i + 1, node[char], 0)
                elif char == s[i]:
                    ans += helper(i + 1, node[char], p)

            return ans

        trie = {}
        
        n = len(t)
        for i in range(n):
            node = trie
            for char in t[i:]:
                if char not in node: 
                    node[char] = {}
                
                node = node[char]
                
                node["$"] = node.get("$", 0) + 1
                
        ans = 0
        m = len(s)      

        for i in range(m):
            ans += helper(i, trie, 1)
        return ans  

