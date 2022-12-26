# https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def helper(word):
            ans = (0, )*26
            
            for char in word: 
                index = ord(char) - ord("a")
                
                ans = ans[: index] + (1, ) + ans[index + 1:]
                
            return ans 
    
        counter = defaultdict(lambda: 0)
        
        for word in words: 
            counter[helper(word)] += 1 
            
        ans = 0 
        
        for key in counter: 
            ans += counter[key]*(counter[key] - 1)//2
            
        return ans 
