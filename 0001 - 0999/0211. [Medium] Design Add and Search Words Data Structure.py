# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(lambda:{})

    def addWord(self, word: str) -> None:
        n = len(word)
        self.dic[n][word] = True
        
    def search(self, word: str) -> bool:
        def helper(word1, word2):
            for i in range(n):
                if word1[i] != ".": 
                    if word1[i] != word2[i]:
                        return False
            return True 
        
        n = len(word)    
        for word_ in self.dic[n]:
            if helper(word, word_):
                return True
            
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
