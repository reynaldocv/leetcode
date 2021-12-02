# https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        def recursive(bottom, new, i):            
            if len(bottom) == 1: 
                return True
            elif i == len(bottom) - 1:
                return recursive(new, "", 0)
            else: 
                colours = dic.get(bottom[i:i + 2], [])
                for color in colours: 
                    if recursive(bottom, new + color, i + 1):
                        return True
                return False
               
        dic = {}
        for triple in allowed: 
            dic[triple[0:2]] = dic.get(triple[0:2], [])
            dic[triple[0:2]].append(triple[2:])

        return recursive(bottom, "", 0)
                
         
