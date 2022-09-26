# https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def helper(son):
            while son != parents[son]:
                son = parents[son]
                
            return son 
            
        index = {chr(ord("a") + i): i for i in range(26)}
        
        parents = [i for i in range(26)]
        
        equals = [equation for equation in equations if "==" in equation]
        
        constraints = [equation for equation in equations if "!=" in equation]
        
        for equal in equals: 
            u = index[equal[0: 1]]
            v = index[equal[3:]]
            
            parentU = helper(u)
            parentV = helper(v)
            
            parents[parentU] = parents[parentV] = min(parentU, parentV)        
 
        for constraint in constraints:             
            u = index[constraint[0: 1]]
            v = index[constraint[3:]]
            
            parentU = helper(u)
            parentV = helper(v)
            
            if parentU == parentV: 
                return False 
            
        return True
        
        
        
                
                
                
