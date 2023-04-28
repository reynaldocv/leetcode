# https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def helper(son):
            while parents[son] != son: 
                son = parents[son]
                
            return son 
        
        def collaborator(word1, word2):
            m, n = len(word1), len(word2)
            
            if m != n: 
                return False 
            
            diff = 0 
            
            first = None 
            second = None 
            
            for i in range(n):
                if word1[i] != word2[i]:
                    diff += 1
                    
                    if first: 
                        second = (word2[i], word1[i])
                        
                    else: 
                        first = (word1[i], word2[i])
                        
            if diff == 0 or (diff == 2 and first == second):
                return True 
            
            return False 
        
        n = len(strs)
        
        parents = [i for i in range(n)]
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if collaborator(strs[i], strs[j]):
                    parentI = helper(i)
                    parentJ = helper(j)
                    
                    parents[parentI] = parents[parentJ] = min(parentI, parentJ)
                    
        seen = set()
        
        for i in range(n):
            seen.add(helper(i))
            
        return len(seen)
                
                
            
            
            
            
            
            
            
            
            
            
            
                
