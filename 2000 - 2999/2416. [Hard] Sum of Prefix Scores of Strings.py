# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        
        for word in words: 
            node = trie 
            
            for char in word: 
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
                
                if "$" in node: 
                    node["$"] += 1 
                    
                else: 
                    node["$"] = 1
                    
        ans = []
        
        for word in words: 
            node = trie
            
            tmp = 0 
            
            for char in word: 
                node = node[char]
                
                tmp += node["$"]
                
            ans.append(tmp)
            
        return ans 
        
