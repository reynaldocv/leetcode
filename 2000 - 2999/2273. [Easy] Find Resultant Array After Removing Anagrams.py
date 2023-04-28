# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        @cache 
        def helper(word):
            ans = (0, )*26
            
            for char in word: 
                idx = index[char]
                
                ans = ans[: idx] +(ans[idx] + 1, ) + ans[idx + 1: ]
                
            return ans 
        
        index = {chr(ord("a") + i): i for i in range(26)}
        
        stack = [words[0]]
        
        for word in words[1: ]:
            if helper(stack[-1]) != helper(word):
                stack.append(word)
                
        return stack 
        
