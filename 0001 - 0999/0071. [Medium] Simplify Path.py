# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        filo = []
        aux = path.split("/")
        n = len(aux)
    
        for i in range(n):
            if aux[i] != "" and aux[i] != "/":
                if aux[i] == "..":
                    if len(filo) > 0: 
                        filo.pop()
                elif aux[i] == ".":
                    continue
                else:                     
                    filo.append(aux[i])
  
    
        return "/" + "/".join(filo)
