# https://leetcode.com/problems/odd-string-difference/

class Solution:
    def oddString(self, words: List[str]) -> str:
        @cache 
        def helper(word):
            ans = (), 
            
            for i in range(1, n):
                diff = ord(word[i]) - ord(word[i - 1])
                
                ans += (diff, )
                
            return ans 
            
        n = len(words[0])
        
        counter = defaultdict(lambda: 0)
        
        for word in words: 
            counter[helper(word)] += 1 
        
        for word in words: 
            if counter[helper(word)] == 1: 
                return word
