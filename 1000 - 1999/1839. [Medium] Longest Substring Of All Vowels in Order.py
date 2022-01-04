# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        index = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        
        i, n = 0, len(word)
        
        aux = ""
        ans = 0 
        for char in word: 
            if aux != "" and (aux[-1] == char or index[aux[-1]] + 1 == index[char]):
                aux += char            
                if aux[-1] == "u": 
                    ans = max(ans, len(aux))  
                   
            else: 
                aux = "a" if char == "a" else ""
                    
        return ans
                
            
