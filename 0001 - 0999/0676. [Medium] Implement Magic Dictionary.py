# https://leetcode.com/problems/implement-magic-dictionary/

class MapSum:

    def __init__(self):
        self.trie = {}
        
    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for char in key: 
            if char not in node: 
                node[char] = {}
            
            node = node[char]
        
        node["value"] = val
        
    def sum(self, prefix: str) -> int:
        def helper(node):
            nonlocal ans
            if "value" in node: 
                ans += node["value"]
            for char in node: 
                if char != "value":                     
                    helper(node[char])
        
        ans = 0 
        
        node = self.trie
        go = True
        for char in prefix: 
            if char in node: 
                node = node[char]
            else:
                go = False
                break
                
        if go: 
            helper(node)
        
        return ans
