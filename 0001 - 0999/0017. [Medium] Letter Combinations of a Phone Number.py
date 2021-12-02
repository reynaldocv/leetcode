# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combination(aux, letters):
            ans = []
            for a in aux: 
                for i in letters: 
                    ans.append(a + i)
            return ans
        
        n = len(digits)
        if n == 0: 
            return []
        else:         
            letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
            ans = [i for i in letters[digits[0]]]
            for i in range(1, n):
                ans = combination(ans, letters[digits[i]])
            return ans
        
        
