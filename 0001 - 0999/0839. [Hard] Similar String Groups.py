# https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def helper(val):
            while val != parent[val]:
                val = parent[val]
                
            return val
        
        def collaborator(val1, val2):
            parent1 = helper(val1)
            parent2 = helper(val2)
            
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        def function(str1, str2):
            ans = 0 
            for (i, char) in enumerate(str1):
                if char != str2[i]:
                    ans += 1 
                    
                if ans > 2: 
                    return False 
                
            return True
            
        n = len(strs)
        parent = [i for i in range(n)]
        
        for i in range(n): 
            for j in range(i): 
                parentI = helper(i)
                parentJ = helper(j)
                if function(strs[i], strs[j]) and parentI != parentJ:
                    collaborator(parentI, parentJ)
        
        ans = 0 
        for i in range(n):
            if i == parent[i]:
                ans +=1 
            
        return ans
