# https://leetcode.com/problems/guess-the-word/

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def helper(word1, word2):
            ans = 0 
            for i in range(n):
                if word1[i] == word2[i]:
                    ans += 1
            
            return ans
        
        m = len(wordlist)
        n = len(wordlist[0])
        
        for _ in range(10):
            word = choice(wordlist)
            score = master.guess(word)
            
            if score == 6: 
                return 
            
            tmp = []
            m = len(wordlist)
            
            for i in range(m):
                if m == 1: 
                    return 
                if wordlist[i] == word: 
                    continue
                if helper(wordlist[i], word) == score: 
                    tmp.append(wordlist[i])
            
            wordlist = tmp
         
