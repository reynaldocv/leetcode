# https://leetcode.com/problems/maximum-product-of-word-lengths/

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
            
        
