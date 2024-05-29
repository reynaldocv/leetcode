# https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        possible = [[1], [2], [1, 2], [3], [1, 3], [4], [1, 4], [5], [2, 3], [6], [1, 2, 3], [1, 5], [2, 4], [7], [1, 6], [2, 4],[1, 2, 4], [3, 4]]
        
        ans = inf
        
        for arr in possible: 
            tmp = []
            
            for elem in arr: 
                tmp.extend([elem for _ in range(elem)])
                
            for perm in permutations(tmp, len(tmp)):
                aux = ""
                
                for elem in perm: 
                    aux += str(elem)
                    
                intAux = int(aux)
                
                if intAux > n: 
                    ans = min(ans, intAux)
                    
        return ans 
        
        
