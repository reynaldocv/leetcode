# https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        trie = {}
        
        node = trie
        for char in s: 
            if char not in node: 
                node[char] = {}
                
            node = node[char]
            node["$"] = True
            
        ans = 0     
        
        for word in words:
            node = trie
            go = True 
            for char in word: 
                if char in node: 
                    node = node[char]
                else: 
                    go = False 
                    break
                    
            ans += 1 if go else 0 
                
        return ans 
