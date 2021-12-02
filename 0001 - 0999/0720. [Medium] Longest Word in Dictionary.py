# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def helper(val, node):
            nonlocal ans
            if ans[0] == len(val):
                ans = (ans[0], min(ans[1], val))
            else: 
                ans = max(ans, (len(val), val))
                
            for char in node: 
                newNode = node[char]
                if char != "isWord" and "isWord" in newNode:
                    helper(val + char, newNode)
               
        trie = {}
        for word in words: 
            node = trie
            for char in word:
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
            node["isWord"] = True
        
        ans = (0, "")
        
        helper("", trie)
        
        return ans[1]
        
