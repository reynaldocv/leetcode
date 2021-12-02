# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        spaces = 0
        words = []
        n = len(text)
        aux = ""
        for i in range(n):
            if text[i] == " ":
                spaces += 1
                if aux != "":
                    words.append(aux)
                aux = ""
            else: 
                aux += text[i]                
        if aux != "":
            words.append(aux)
        if len(words) == 1:
            q = 1
            r = spaces
        else:
            q = spaces//(len(words) - 1)
            r = spaces % (len(words) - 1)
            
        ans = (" "*q).join(words) + " "*r
        return ans
                
