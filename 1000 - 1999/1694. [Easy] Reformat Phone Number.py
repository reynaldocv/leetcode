# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        def helper(word):
            if len(word) <= 3:
                return word
            
            elif len(word) == 4: 
                return word[: 2] + "-" + word[2: ]
                
            else: 
                return word[: 3] + "-" + helper(word[3: ])
            
        word = ""
        
        for char in number + " ": 
            if char != " " and char != "-":
                word += char 
                
        return helper(word)
