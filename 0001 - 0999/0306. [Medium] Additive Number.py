# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(first, second, word):
            if word == "":
                return True 
            
            third = str(int(first) + int(second))
            
            m, l = len(third), len(word)
            
            if m <= l: 
                for i in range(m):
                    if third[i] != word[i]:
                        return False 
                    
                if helper(second, int(third), word[m: ]):
                    return True 
                
            return False 
        
        n = len(num)
        
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                first = num[: i]
                second = num[i: j]
                
                if len(str(int(first))) == len(first) and len(str(int(second))) == len(second):                
                    if helper(first, second, num[j: ]):
                        return True 
                
        return False
