# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        index = {}        
        masks = []
        
        for companies in favoriteCompanies: 
            mask = 0
            
            for companie in companies: 
                if companie not in index: 
                    index[companie] = len(index) + 1
                    
                mask ^= 1 << index[companie]
            
            masks.append(mask)
            
        ans = []
        
        for (i, maskA) in enumerate(masks):            
            add = True
        
            for (j, maskB) in enumerate(masks): 
                if i != j: 
                    if maskA & maskB == maskA: 
                        add = False
            
                        break
                    
            if add: 
                 ans.append(i)
                        
        return ans
           
