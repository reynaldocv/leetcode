# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        node = self.trie 
        
        for char in word: 
            if char not in node: 
                node[char] = {}
                
            node = node[char]
            
        node["$"] = True 

    def search(self, word: str) -> bool: 
        def helper(node, word):            
            if word == "": 
                return "$" in node
            
            else: 
                char = word[0]
                
                if char == ".":                
                    for char in node: 
                        if char != "$":
                            if helper(node[char], word[1: ]):
                                return True 

                elif char in node: 
                    if helper(node[char], word[1: ]):
                        return True 
                
                return False 
            
        return helper(self.trie, word)
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
    
