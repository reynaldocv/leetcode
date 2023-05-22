# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        letters = {}
        letters["2"] = "abc"
        letters["3"] = "def"
        letters["4"] = "ghi"
        letters["5"] = "jkl"
        letters["6"] = "mno"
        letters["7"] = "pqrs"
        letters["8"] = "tuv"
        letters["9"] = "wxyz"
        
        ans = [""]
        
        for char in digits:             
            tmp = []
            
            for sequence in ans: 
                for letter in letters[char]:
                    tmp.append(sequence + letter)
                    
            ans = tmp 
            
        return ans        
