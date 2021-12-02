# https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary:

    def __init__(self):
        self.words = defaultdict(lambda: [])

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary: 
            self.words[len(word)].append(word)
        
    def search(self, searchWord: str) -> bool:
        def helper(word1, word2):
            cnt = 0
            for (i, char) in enumerate(word1):
                if char != word2[i]:
                    cnt += 1
                    if cnt > 1: 
                        return False
            
            return cnt == 1
        
        for word in self.words[len(searchWord)]:
            if helper(searchWord, word):
                return True
            
        return False
        
       
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
