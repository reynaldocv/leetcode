# https://leetcode.com/problems/stream-of-characters/

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words: 
            node = self.trie
            for char in word[::-1]: 
                if char not in node: 
                    node[char] = {}
                
                node = node[char]
            
            node["$"] = word
            
        self.letters = []
        
    def query(self, letter: str) -> bool:        
        self.letters.insert(0, letter)
        
        node = self.trie
        
        for char in self.letters: 
            if char in node:                 
                node = node[char]
                if "$" in node: 
                    return True
            else: 
                break
                
        return False
