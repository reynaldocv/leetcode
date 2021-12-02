# https://leetcode.com/problems/concatenated-words/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]: 
        @cache        
        def find(word):
            if not word: 
                return True
            
            tmp = trie
            val = False
            for (i, char) in enumerate(word):
                if char not in tmp: 
                    break
                tmp = tmp[char]
                if "isWord" in tmp: 
                    val |= find(word[i + 1:])
                    if val:
                        break
            
            return val
        
        trie = {}
        for word in words: 
            node = trie
            for char in word:
                if char not in node: 
                    node[char] = {}
                
                node = node[char]
                
            node["isWord"] = True
            
        ans = []
        for word in words: 
            node = trie
            for (i, char) in enumerate(word): 
                node = node[char]
                if "isWord" in node: 
                    if i != len(word) - 1 and find(word[i + 1:]):
                        ans.append(word)
                        break
        
        return ans
        
