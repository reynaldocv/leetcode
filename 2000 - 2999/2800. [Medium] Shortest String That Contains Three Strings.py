# https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def helper(wordA, wordB):
            if wordA in wordB: 
                return wordB
            
            elif wordB in wordA: 
                return wordA
            
            else: 
                m = min(len(wordA), len(wordB))
                
                for i in range(m - 1, -1, -1):
                    if wordA[-i: ] == wordB[: i]:
                        return wordA + wordB[i: ]
                    
                return wordA + wordB
                    
        words = [a, b, c]
        
        total = len(a) + len(b) + len(c) + 1
        
        ans = (total, "$"*total) 
        
        for (i, j, k) in permutations([0, 1, 2], 3):
            word = helper(words[i], words[j])
            word = helper(word, words[k]) 
            
            ans = min(ans, (len(word), word))
            
        return ans[1]
            
