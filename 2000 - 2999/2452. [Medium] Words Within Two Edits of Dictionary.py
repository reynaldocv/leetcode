# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def helper(word, node, times):
            if word == "":
                return True 
            
            else: 
                for char in node: 
                    if times > 0:
                        if helper(word[1: ], node[char], times - 1):
                            return True 
                        
                    if char == word[0]:
                        if helper(word[1: ], node[char], times):
                            return True 
                
                return False 
        
        trie = {}
        
        for word in dictionary: 
            node = trie
            
            for char in word: 
                if char not in node: 
                    node[char] = {}
                    
                node = node[char]
            
            
        ans = []
            
        for querie in queries: 
            if helper(querie, trie, 2) == True:
                ans.append(querie)
                
        return ans 
                    
