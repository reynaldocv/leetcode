# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        
        ans = ""
        
        word = ""        
        times = 1
        
        for char in sentence + " ":
            if char != " ":
                word += char
                
            else:
                if word[0] in vowels:
                    ans += word + "ma"
                
                else:
                    ans += word[1: ] + word[0] + "ma"
                    
                word = ""
                ans += "a"*times + " "
                
                times += 1
                
        return ans[: -1]
