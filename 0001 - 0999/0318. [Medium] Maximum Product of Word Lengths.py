# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        uniqueLetters = []
        
        for word in words: 
            seen = set([])
            
            tmp = ""
            
            for char in word: 
                if char not in seen: 
                    tmp += char 
                    
                seen.add(char)
                
            uniqueLetters.append(tmp)
            
        n = len(words)
        
        index = defaultdict(lambda: set())
        
        for (i, word) in enumerate(words):
            for char in uniqueLetters[i]: 
                index[char].add(i)
                
        ans = 0         
        
        for (i, word) in enumerate(words): 
            index2 = {i for i in range(n)}
            
            for char in uniqueLetters[i]: 
                for idx in index[char]:
                    if idx in index2:
                        index2.remove(idx)
                        
            for num in index2: 
                ans = max(ans, len(words[num])*len(word))
            
        return ans 
        
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def helper(word1, word2):
            for char in word1: 
                if char in word2: 
                    return False
            return True
        
        ans = 0
        for (idx, word1) in enumerate(words):
            for word2 in words[idx + 1:]:
                if helper(word1, word2):
                    ans = max(ans, len(word1)*len(word2))
                    
        return ans
            
        
