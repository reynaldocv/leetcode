# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        cnt = 0 
        
        ans = 0 
        
        for (i, char) in enumerate(s):
            if char in "aeiou":
                cnt += 1 
            
            ans = max(ans, cnt - counter[i - k])
                        
            counter[i] = cnt
            
        return ans 
        
                    
                
                
