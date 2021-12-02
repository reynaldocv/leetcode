# https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        def removeLastSpaces(a):
            idx = -1
            for i in range(len(a)):
                if a[i] != " ":
                    idx = i
            
            return a[:idx + 1]
        
        words = s.split(" ")        
        n = len(words)
        m = max([len(word) for word in words])
        ans = []
        for i in range(m):
            aux = ""
            for j in range(n):
                aux += words[j][i] if i < len(words[j]) else " "
            aux = removeLastSpaces(aux)
            ans.append(aux)
        
        return ans
                
        
