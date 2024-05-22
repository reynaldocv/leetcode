# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        cnt = 0 
        prev = "$"
        
        chars = []
        counter = [0]
        
        for char in word + "$":            
            if prev != char:
                if cnt > 0:
                    chars.append(prev)
                    counter.append(cnt)   
            
            cnt += 1
            prev = char
        
        n = len(chars)
        
        ans = 0
        
        for i in range(n):
            if "".join(chars[i: i + 5]) == "aeiou":
                tmp = counter[i + 5] - counter[i]
                
                ans = max(ans, tmp)
            
        return ans
                
            
