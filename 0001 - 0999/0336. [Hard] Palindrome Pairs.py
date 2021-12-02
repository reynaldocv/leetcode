# https://leetcode.com/problems/palindrome-pairs/336. Palindrome Pairs

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = set()
        n = len(words)
        
        sentences = {words[i]: i for i in range(n)}
        
        for (i, word) in enumerate(words):
            rev = word[::-1]
            m = len(word)
            for j in range(m + 1):                
                if word[j:] == rev[:m - j]:
                    if rev[m - j:] in sentences:                         
                        ans.add((i, sentences[rev[m - j:]]))
                if word[:m - j] == rev[j:]:
                    if rev[:j] in sentences: 
                        ans.add((sentences[rev[:j]], i))
                        
        return [(a, b) for (a, b) in ans if a != b]
                
            
