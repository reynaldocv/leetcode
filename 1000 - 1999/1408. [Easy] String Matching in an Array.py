# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        
        words.sort(key = lambda item: -len(item))
        
        ans = []
        
        for i in range(1, n):
            for j in range(i):
                if words[i] in words[j]:
                    ans.append(words[i])
                    
                    break 
                    
        return ans 
