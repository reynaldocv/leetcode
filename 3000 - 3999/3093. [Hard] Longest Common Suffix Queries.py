# https://leetcode.com/problems/longest-common-suffix-queries/

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {"$": (inf, 0)}
        
        for (i, word) in enumerate(wordsContainer): 
            trie["$"] = min(trie["$"], (len(word), i))
            
            node = trie
            
            for char in word[:: -1]: 
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
                
                if "$" in node: 
                    node["$"] = min(node["$"], (len(word), i))
                    
                else: 
                    node["$"] = (len(word), i)
                    
        ans = []
        
        for word in wordsQuery: 
            node = trie
            
            for char in word[:: -1]: 
                if char not in node: 
                    break 
                
                node = node[char]
                
            ans.append(node["$"][1])
            
        return ans
                    
        
