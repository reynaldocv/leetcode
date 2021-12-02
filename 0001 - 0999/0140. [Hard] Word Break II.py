# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache 
        def helper(word):
            ans = []
            if word in seen:
                ans.append(word)            
            
            for i in range(1, min(len(word), 11)):

                newWord = word[:i] 
                if newWord in seen: 
                    arr = [newWord + " " + sentence for sentence in helper(word[i:])]
                    ans.extend(arr)

            return ans

        seen = {}
        for word in wordDict: 
            seen[word] = True
            
        ans = helper(s)
        
        return ans
            
        
        
        
