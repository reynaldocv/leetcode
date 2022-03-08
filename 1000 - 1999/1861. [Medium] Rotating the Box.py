# https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        for i in range(m):            
            prev = 0 
            box[i].append("*")
            for j in range(n + 1):
                if box[i][j] == "#":
                    prev += 1 
                    box[i][j] = "."
                if box[i][j] == "*":
                    aux = j - 1
                    while prev > 0: 
                        box[i][aux] = "#"
                        aux -= 1 
                        prev -= 1 
           
        ans = []
        
        for j in range(n):
            aux = []
            for i in range(m):
                aux.append(box[m - i - 1][j])
                
            ans.append(aux)
            
        return ans
