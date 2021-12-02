# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        left = "({["
        filo = []
        for i in range(len(s)):
            if s[i] in left:
                filo.append(s[i])
            else: 
                if len(filo) > 0:
                    aux = filo[len(filo) - 1]
                    if aux == "(" and s[i] == ")":
                        filo.pop()
                    elif aux == "[" and s[i] == "]":
                        filo.pop()                
                    elif aux == "{" and s[i] == "}":
                        filo.pop()
                    else:
                        return False
                    
                else:
                    return False
        return True if (len(filo) == 0) else False
        
