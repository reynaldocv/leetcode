# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set([])
        for word in words: 
            for word2 in words: 
                if len(word) < len(word2):
                    if word in word2: 
                        ans.add(word)
        return ans
            
        
